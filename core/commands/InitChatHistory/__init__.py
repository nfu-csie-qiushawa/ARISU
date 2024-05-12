import discord, json
from discord.ext import commands
from discord import app_commands

class InitChatHistory(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @app_commands.command(name = "重製對話紀錄", description = "此命令可以重製此頻道的對話紀錄")
    @app_commands.guild_only()
    async def initChatHistory_commands(self, interaction: discord.Interaction):
        with open("database\chat_history.json", 'r', encoding='utf-8') as db:
            data = json.load(db)
        data["history"][f"{interaction.channel.id}"]=[]
        with open("database\chat_history.json", 'w', encoding='utf-8') as db:
            json.dump(data, db, indent=4)
        await interaction.response.send_message("已初始化對話紀錄")
async def setup(bot:commands.Bot):
    print(f"load: {InitChatHistory.__name__}")
    await bot.add_cog(InitChatHistory(bot))