import discord
from discord.ext import commands


class Music(commands.Cog):
    @commands.command()
    async def play(self, ctx):
        try:
            channel = ctx.author.voice.channel
        except AttributeError:
            return

        if channel:
            voice_client = await channel.connect()
        else:
            return

        if voice_client.is_playing():
            voice_client.stop()

        try:
            voice_client.play(discord.FFmpegPCMAudio("cogs/testsong.mp3"))
        except Exception as e:
            print(e)


def setup(bot):
    bot.add_cog(Music())
