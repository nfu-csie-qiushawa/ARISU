
async def register_commands(self):
    slash = await self.bot.tree.sync()
    print(f"目前登入身份 --> {self.bot.user}")
    print(f"載入 {len(slash)} 個斜線指令")