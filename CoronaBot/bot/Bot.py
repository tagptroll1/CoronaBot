import asyncio
import socket
from typing import Optional

import aiohttp
from discord.ext import commands

class Waifu(commands.Bot):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self._resolver = aiohttp.AsyncResolver()

    # Use AF_INET as its socket family to prevent HTTPS related problems both locally
    # and in production.
    self._connector = aiohttp.TCPConnector(
        resolver=self._resolver,
        family=socket.AF_INET,
    )

    self.http.connector = self._connector
    self.http_session = aiohttp.ClientSession(connector=self._connector)

    