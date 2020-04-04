import re
import asyncio
import datetime as dt

import discord
from discord.ext import commands

class Info(commands.Cog):
    @commands.command()
    async def ping(self, ctx):
        return await ctx.send(f"Pong! latency: {ctx.bot.latency*1000:.2f}ms")

    @commands.command(aliases=['invite'])
    async def join(self, ctx):
        """Joins a server"""
        perms = discord.Permissions.all()
        embed = discord.Embed()
        embed.description = f"Invite me with [this link]({discord.utils.oauth_url(self.bot.app_info.id, permissions=perms)})"
        await ctx.send(embed=embed)

    @commands.command()
    async def remindme(self, ctx, time: str, *, message: str=None):
        """remind_me <time> [message]

        Time units:
            d - days
            h - hours
            m - minutes
            s - seconds

        syntax: <number><timeunit>[message]
        examples:
            remind_me 20m55s do stuff
            remind_me 1d20s do stuff tomorrow
            remind_me 2d10h23m55s very specificly in this time
        """
        message = message or "No message attached!"
        pattern = re.compile(
            r'((?P<days>\d+)d)?((?P<hours>\d+)h)?((?P<minutes>\d+)m)?((?P<seconds>\d+)s)?')

        match = pattern.fullmatch(time)
        if not match:
            return 

        kwargs = {
            "days": int(match.group("days")) if match.group("days") is not None else 0,
            "hours": int(match.group("hours")) if match.group("hours") is not None else 0,
            "minutes": int(match.group("minutes")) if match.group("minutes") is not None else 0,
            "seconds": int(match.group("seconds")) if match.group("seconds") is not None else 0,
        }

        reminder_string = ""
        reminder_string += f'{kwargs["days"]:g} days ' if kwargs.get(
            "days") else ""
        reminder_string += f'{kwargs["hours"]:g} hours ' if kwargs.get(
            "hours") else ""
        reminder_string += f'{kwargs["minutes"]:g} minutes ' if kwargs.get(
            "minutes") else ""
        reminder_string += f'{kwargs["seconds"]:g} seconds ' if kwargs.get(
            "seconds") else ""
        await ctx.send(f"A reminder for {reminder_string} has been set", delete_after=10)

        delta = dt.timedelta(**kwargs)
        sleeptime = delta.total_seconds()
        await asyncio.sleep(sleeptime)

        await ctx.send(f"It's been {reminder_string} seconds since "
                       f"{ctx.author.mention} made this reminder:\n{message}")


def setup(bot):
    bot.add_cog(Info())
