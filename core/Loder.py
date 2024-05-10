import discord, os
import asyncio
from discord.ext import commands
__command=os.listdir("./commands")
__events=os.listdir("./events")
async def commands_loder(bot:commands.Bot):
    for extension in __command:
        await bot.load_extension(f'commands.{extension}')
        
async def event_loder(bot:commands.Bot):
    for extension in __events:
        await bot.load_extension(f'events.{extension}')