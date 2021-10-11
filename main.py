import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run("ODk3MTY2MDkwNTkxOTUyOTQ3.YWRtCA.aaUYja7_ANy1ma1MZAXPe2f5Sss")
