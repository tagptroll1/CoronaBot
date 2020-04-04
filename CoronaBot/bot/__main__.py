import sys
from pathlib import Path

from discord.ext import commands
from bot.Bot import Waifu
from bot.constants import Bot as bot_config

if sys.platform.startswith("win") and sys.version_info >= (3, 8):
    import asyncio
    try:
        from asyncio import WindowsSelectorEventLoopPolicy
    except ImportError:
        pass  # Can't assign a policy which doesn't exist.
    else:
        if not isinstance(asyncio.get_event_loop_policy(), WindowsSelectorEventLoopPolicy):
            asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

bot = Waifu(
  command_prefix=commands.when_mentioned_or(bot_config.prefix),
  case_insensitive=True
)

cogs = Path("./bot/cogs")
for cog in cogs.iterdir():
    if cog.is_dir():
        continue

    if cog.suffix == ".py":
        path = ".".join(cog.with_suffix("").parts)
        try:
            bot.load_extension(path)
            print(f"{'Loaded...':<19} {path:<1}!")
        except Exception as e:
            print(f"{'Failed to load...':<19} {path:<1}!")
            print(e, "\n")


bot.run(bot_config.token)
