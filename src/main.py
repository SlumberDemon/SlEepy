import discord 
from discord.ext import commands

bot = commands.Bot(command_prefix='-')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('OTAzMTg3NzU2MjU0MTMwMTc3.YXpVJQ.4sob8XqW7XmAzLd6HpisoC0ISKU')