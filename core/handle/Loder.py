import discord, os
import asyncio
import zipfile
from discord.ext import commands
__mods=[_ for _ in os.listdir("./mods") if _.endswith('.zip')]
async def loder(bot:commands.Bot):
    for file in __mods:
        if 'command' in file: url='./core/commands'
        elif 'events' in file: url='./core/events'
        else: return print("檔名格式錯誤")
        path=f'mods/{file}'
        if not zipfile.is_zipfile(path): return print("檔案毀損")
        ZIP = zipfile.ZipFile(path)
        modname=file.replace("_command", "").replace("_event", "").replace(".zip", "")
        try:
            if modname not in os.listdir(url):ZIP.extractall(url,pwd=f"{os.getenv('BOT_ID')}".encode("utf-8"))
        except:
            print("你缺少權限")
        ZIP.close()
    await commands_loder(bot, os.listdir("./core/commands"))
    await event_loder(bot, os.listdir("./core/events"))
async def commands_loder(bot:commands.Bot,command):
    for extension in command:
        await bot.load_extension(f'core.commands.{extension}')
        
async def event_loder(bot:commands.Bot, events):
    for extension in events:
        await bot.load_extension(f'core.events.{extension}')