import discord, asyncio
from discord.ext import commands
from PIL import Image
import requests
from io import BytesIO


from .gemini import *
class onMessage(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.text_model = genai.GenerativeModel('gemini-pro')
        self.img_model = genai.GenerativeModel('gemini-pro-vision')
        self.bot = bot
        self.chat=self.text_model.start_chat(history=[])
    @commands.Cog.listener()
    async def on_message(self, message:discord.Message):
        if message.author==self.bot.user:
            return
        if message.content.startswith(f"<@{self.bot.user.id}>"):
            if len(message.attachments):
                url=message.attachments[0].url
                r = askToGemini_img(message.content.replace(f"<@{self.bot.user.id}>", ""), url, message.channel.id)
                await message.reply(r)
            else:
                r = askToGemini_text(message.content.replace(f"<@{self.bot.user.id}>", ""), self.chat,  message.channel.id)
                await message.reply(r)
            self.history=change_history([r], 'model', message.channel.id)
async def setup(bot:commands.Bot):
    await bot.add_cog(onMessage(bot))