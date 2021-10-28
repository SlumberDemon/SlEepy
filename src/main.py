import discord 
from discord.ext import commands
from os import getenv


# Intents

intents = discord.Intents.default()
intents.members = True

# Setup

bot = commands.Bot(command_prefix='-', intents=intents)
inter_client = InteractionClient(client, modify_send=False) # modify_send=False to make discord.py 2.0 views work

# Stuff

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(getenv('TOKEN'))