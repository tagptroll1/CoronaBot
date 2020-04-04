import discord 
from discord.ext import commands


class CogCog(commands.Cog):
    @commands.command()
    async def reload(self, ctx: commands.Context, cog_name):
        try:
            ctx.bot.reload_extension(f"bot.cogs.{cog_name}")
            await ctx.send("👍")
        except Exception as e:
            await ctx.send(f"Failed: {e}")

    @commands.command()
    async def load(self, ctx: commands.Context, cog_name):
        try:
            ctx.bot.unload_extension(f"bot.cogs.{cog_name}")
            await ctx.send("👍")
        except Exception as e:
            await ctx.send(f"Failed: {e}")

    @commands.command()
    async def unload(self, ctx: commands.Context, cog_name):
        try:
            ctx.bot.load_extension(f"bot.cogs.{cog_name}")
            await ctx.send("👍")
        except Exception as e:
            await ctx.send(f"Failed: {e}")

    @commands.command()
    async def embedfield(self, ctx, name, value):
        e = discord.Embed()
        e.add_field(name=name, value=value)
        e.add_field(name=name, value=value, inline=False)
        e.add_field(name=name, value=value)
        e.add_field(name=name, value=value)
        await ctx.send(embed=e)

def setup(bot: commands.Bot):
    bot.add_cog(CogCog())
