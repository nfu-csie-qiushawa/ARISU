import discord
from discord.ext import commands
from discord import app_commands


class Ping(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    @app_commands.command(name = "查看延遲", description = "此命令可以查看機器人延遲時間")
    async def ping_command(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"機器人ping值: {round(self.bot.latency, 1)}ms", ephemeral=True)
async def setup(bot:commands.Bot):
    print(f"load: {Ping.__name__}")
    await bot.add_cog(Ping(bot))