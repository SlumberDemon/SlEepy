import discord 
from discord.ext import commands
from dislash import InteractionClient
from os import getenv


# Intents

intents = discord.Intents.default()
intents.members = True

# Setup

bot = commands.Bot(command_prefix='-', intents=intents)
inter_client = InteractionClient(bot, modify_send=False) # modify_send=False to make discord.py 2.0 views work
guilds = [877399405056102431, 819112190115446844]

# Stuff

@bot.command(aliases=['ping'], help='Shows bot latency')
async def latency(ctx):
    embed = discord.Embed(description=f'🏓 Pong! {round(bot.latency * 1000)}ms', colour=0xc3d9df)
    await ctx.send(embed=embed)

# Cogs

bot.load_extension('cogs.Slash')
bot.load_extension('cogs.Events')

bot.run(getenv('TOKEN'))