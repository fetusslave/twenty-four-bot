import os
import asyncio
from dotenv import load_dotenv
import discord
from discord.ext import commands


class Client(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix=commands.when_mentioned_or('.'), intents=intents)

        self.cogs_list = ["cogs.game_cog"]

    async def setup_hook(self):
        for ext in self.cogs_list:
            await self.load_extension(ext)

    async def on_ready(self):
        synced = await self.tree.sync()
        print(synced)


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN", "")

client = Client()
asyncio.run(client.run(TOKEN))
