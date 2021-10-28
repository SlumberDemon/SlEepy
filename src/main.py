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

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@inter_client.slash_command(
    name="hello", # Defaults to the function name
    description="Says hello",
    guild_ids=guilds
)
async def hello(inter):
    await inter.reply("Hello!")

bot.run(getenv('TOKEN'))