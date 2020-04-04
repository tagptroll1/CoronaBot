import discord

from bot.utils.emoji_lookup import flags

class Country:
    def __init__(self, name, total, new_cases, deaths, 
                 new_deaths, recovered, active, critical, 
                 total_1mil, deaths_1mil):
        self.name = name
        self.total = total
        self.new_cases = new_cases
        self.deaths = deaths
        self.new_deaths = new_deaths
        self.recovered = recovered
        self.active = active
        self.critical = critical
        self.total_1mil = total_1mil
        self.deaths_1mil = deaths_1mil
        self.flag = flags.get(name, "")

    def __str__(self):
        return f"{name}: {self.total}"

    @property
    def embed(self):
        e = discord.Embed(title=f"{self.name} {self.flag}", color=discord.Color.purple())
        e.add_field(name="**__Total cases__**\u2000", value=self.total)
        e.add_field(name="**__New cases__**\u2000", value=self.new_cases)
        e.add_field(name="**__Per 1,000,000__**\u2000", value=self.total_1mil)
        e.add_field(name="**__Deaths__**\u2000", value=self.deaths)
        e.add_field(name="**__New deaths__**\u2000", value=self.new_deaths)
        e.add_field(name="**__Per 1,000,000__**\u2000", value=self.deaths_1mil)
        return e
