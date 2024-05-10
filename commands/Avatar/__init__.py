import discord
from discord.ext import commands
from discord import app_commands
from .embed import *
class Avatar(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    @app_commands.command(name = "查看頭像", description = "此命令可以查看成員頭像")
    @app_commands.describe(成員 = "選擇成員")
    async def avatar_commands(self, interaction: discord.Interaction, 成員:discord.Member):

        await interaction.response.send_message(embed=avatar_embed(member=成員))
async def setup(bot:commands.Bot):
    print(f"load: {Avatar.__name__}")
    await bot.add_cog(Avatar(bot))