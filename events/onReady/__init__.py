import discord
from discord.ext import commands

from .register import *
from .activity import *

class onReady(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        await register_commands(self)
        await change_activity(self)
async def setup(bot:commands.Bot):
    await bot.add_cog(onReady(bot))