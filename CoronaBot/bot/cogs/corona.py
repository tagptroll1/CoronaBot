import aiohttp
import asyncio
from typing import Dict

from bs4 import BeautifulSoup
from datetime import datetime
from discord.ext import commands, tasks

from bot.models.corona_country import Country


URL = "https://www.worldometers.info/coronavirus/#countries"


def process_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    countries = {}

    rows = soup.find_all("tr")

    for row in rows:
        columns = row.find_all("td")

        if len(columns) <= 1:
            continue

        name, total, new, deaths, new_deaths, recovered, active, critical, tot1m, death1m, *_ = columns

        country = Country(
            name.text.rstrip(":"),
            total.text,
            new.text,
            deaths.text,
            new_deaths.text,
            recovered.text,
            active.text,
            critical.text,
            tot1m.text,
            death1m.text
        ) 
        countries[country.name.lower()] = country

    last_fetch = datetime.now()

    return countries


class CoronaCog(commands.Cog):
    # Reload subscribes the events twice (Fixed by removing task, but this breaks persistence)
    # Mention everyone that subscribed to a country
    # Previous change
    # Longer interval
    # Subscriptions = { country: {subs: [{guildid: {channelid: [userid]}}], last_number}}
    def __init__(self, bot):
        self.bot = bot
        self.last_fetched = datetime.now()
        self.cache_timeout = 60
        self.countries: Dict[string, Country] = {}
        self.subscriptions = {}
        # self.subscribe_corona.start()

    def cog_unload(self):
        """hook for unloading cog"""
        ...
        # Store subs here for when it loads up next time
        #   self.subscribe_corona.cancel()

    async def refresh_countries(self):
        cache_timediff = datetime.now() - self.last_fetched

        if not self.countries or cache_timediff.seconds > self.cache_timeout:
            response = await self.bot.http_session.get(URL)
            html = await response.text()
            self.countries = await self.bot.loop.run_in_executor(
                None, process_html, html
            )
            self.last_fetched = datetime.now()

    # TODO
    # @tasks.loop(minutes=1)
    async def subscribe_corona(self):
        await self.refresh_countries()

        for subscription in self.subscriptions.values():
            user = subscription["user"]
            countries = subscription["countries"]
            channel = subscription["channel"]

            message = f"Hey {user.mention}, something has changed on your subscribed countries!\n"

            new_countries = {}
            send = False
            for country in countries:
                last_value = countries[country]
                current_value = self.countries.get(country)

                if last_value != current_value:
                    print("===DURING===")
                    print(
                        user.display_name,
                        f"self.subs.countries: {self.subscriptions[user.id]['countries'][country]}",
                        f"subscription.countries: {subscription['countries']}",
                        sep="\n"
                    )
                    send = True
                    message += f"{country}: {current_value}\n"

                new_countries[country] = current_value

            subscription["countries"] = new_countries

            if send:
                await channel.send(message)

    # TODO
    # @commands.command(aliases=["subs"])
    async def subscriptions(self, ctx):
        user_subscriptions = self.subscriptions.get(ctx.author.id)

        if not user_subscriptions:
            return await ctx.send("You don't have any subscriptions")

        countries = user_subscriptions["countries"]
        await ctx.send(f"Your current subscriptions: {', '.join(countries)}")

    # TODO renable
    # @commands.command(aliases=["sub"])
    async def subscribe(self, ctx, *, country=None):
        if not country:
            return await ctx.send("You must specify a country or 'total' to subscribe")

        user_subscriptions = self.subscriptions.get(ctx.author.id)
        country = country.lower()

        if not user_subscriptions:
            user_subscriptions = {
                "user": ctx.author,
                "countries": {},
                "channel": ctx.channel
            }
            self.subscriptions[ctx.author.id] = user_subscriptions

        if user_subscriptions["countries"].get(country):
            return await ctx.send(f"You're already subscribed to {country}")

        if country not in self.countries:
            return await ctx.send("This country is not subscribeable!")

        user_subscriptions["countries"][country] = self.countries.get(country)

        await ctx.send(
            f"Subscribed to {country}, "
            f"your current subscriptions are {','.join(user_subscriptions['countries'])}"
        )

    # TODO Renable
    # @commands.command(aliases=["unsub"])
    async def unsubscribe(self, ctx, *, country=None):
        if not country:
            return await ctx.send("You must specify a country or 'total' to subscribe")

        user_subscriptions = self.subscriptions.get(ctx.author.id)

        if not user_subscriptions:
            return await ctx.send("You don't have any subscriptions")

        countries = user_subscriptions["countries"]
        country_value = countries.get(country)

        if not country_value:
            return await ctx.send(f"You're not subscribed to {country}")

        def check(c):
            n, v = c
            return n != country

        countries = dict(filter(check, countries.items()))
        user_subscriptions["countries"] = countries

        await ctx.send(f"Unsubscribed, you're currently subscribed to {', '.join(countries)}")

    @commands.command()
    async def corona(self, ctx, *, name="total"):
        await self.refresh_countries()

        country = self.countries.get(name.lower())

        if country:
            await ctx.send(embed=country.embed)
        else:
            await ctx.send(f"Country not found, available countries can be found here <{URL}>")


def setup(bot: commands.Bot):
    bot.add_cog(CoronaCog(bot))
