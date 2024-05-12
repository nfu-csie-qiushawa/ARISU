import discord, os
import asyncio
from discord.ext import commands
__command=os.listdir("./core/commands")
__events=os.listdir("./core/events")
async def mods_loder():
    ...
async def commands_loder(bot:commands.Bot):
    for extension in __command:
        await bot.load_extension(f'core.commands.{extension}')
        
async def event_loder(bot:commands.Bot):
    for extension in __events:
        await bot.load_extension(f'core.events.{extension}')
