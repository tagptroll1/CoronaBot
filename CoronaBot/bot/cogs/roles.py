from discord.ext import commands


class Roles(commands.Cog):
    def __local_check(self, ctx) -> bool:
        if not ctx.guild:
            return False
        if not ctx.guild.me.guild_permissions.manage_roles:
            return False
        return True


def setup(bot):
    bot.add_cog(Roles())
