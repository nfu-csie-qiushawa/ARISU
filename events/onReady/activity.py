import discord
async def change_activity(self):
    await self.bot.change_presence(activity=discord.Game(name="蔚藍檔案"))