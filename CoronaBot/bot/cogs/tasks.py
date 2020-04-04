import discord
import random
from discord.ext import commands, tasks


class Tasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        with open("compliments.txt", "r") as comps:
            self.compliments = comps.readlines()

        self.guilds = {}
        self.channels = {}
        self.persons = {}

        # self.compliment_wabbu.start()
        # self.compliment_pesn.start()

    async def get_guild(self, id_):
        guild = self.guilds.get(id_)

        if guild:
            return guild

        guild = self.bot.get_guild(id_)

        if not guild:
            guild = await self.bot.fetch_guild(id_)

        self.guilds[id_] = guild
        return guild

    async def get_channel(self, id_, guild):
        channel = self.channels.get(id_)

        if channel:
            return channel

        channel = guild.get_channel(id_)

        if not channel:
            channel = await guild.fetch_channel(id_)

        self.channels[id_] = channel
        return channel

    async def get_person(self, id_, guild):
        person = self.persons.get(id_)

        if person:
            return person

        person = guild.get_member(id_)

        if not person:
            person = await guild.fetch_member(id_)

        self.persons[id_] = person
        return person

    async def compliment(self, guild_id, channel_id, person_id):
        guild = await self.get_guild(guild_id)
        channel = await self.get_channel(channel_id, guild)
        person = await self.get_person(person_id, guild)

        if person.status == discord.Status.offline:
            return

        compliment = random.choice(self.compliments)
        await channel.send(f"{person.mention} {compliment}")

    # @tasks.loop(hours=1)
    async def compliment_wabbu(self):
        await self.bot.wait_until_ready()

        nomanskype = 231152642175401989
        channel_id = 231152642175401989
        wabbu_id = 123114562701492224

        await self.compliment(nomanskype, channel_id, wabbu_id)

    # @tasks.loop(hours=1)
    async def compliment_pesn(self):
        await self.bot.wait_until_ready()

        friendly_stalkers = 234366743445897216
        secret_magic = 453232648584953886
        pesn = 632191780988911617

        await self.compliment(friendly_stalkers, secret_magic, pesn)

def setup(bot):
    bot.add_cog(Tasks(bot))