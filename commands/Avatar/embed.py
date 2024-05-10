import discord
import datetime
def avatar_embed(member:discord.Member):
    if member.nick:
        name=member.nick
    else:
        name=member.name
    embed=discord.Embed(title=name, color=member.color, timestamp=datetime.datetime.now())
    embed.set_image(url=member.avatar.url)
    return embed