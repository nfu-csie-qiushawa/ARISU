import discord
from discord.ext import commands
import asyncio
import logging
import os
from dotenv import load_dotenv
from core.handle.Loder import commands_loder, event_loder
load_dotenv()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", intents = intents)

async def main():
    FORMAT = '%(asctime)s %(levelname)s: %(message)s'
    logging.basicConfig(level=logging.DEBUG, filename='Log.log', filemode='a', format=FORMAT)
    async with bot:
        await commands_loder(bot)
        await event_loder(bot)
        await bot.start(os.getenv("DISCORD_TOKEN"))

if __name__ == "__main__":
    asyncio.run(main())
