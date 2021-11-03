import discord 
from discord.ext import commands
from dislash import InteractionClient
from os import getenv


# Intents

intents = discord.Intents.default()
intents.members = True

# Setup

bot = commands.Bot(command_prefix='-', intents=intents, help_command=None)
inter_client = InteractionClient(bot, modify_send=False) # modify_send=False to make discord.py 2.0 views work

# Cogs

bot.load_extension('cogs.Slash')
bot.load_extension('cogs.Events')
bot.load_extension('cogs.Error')

bot.run(getenv('TOKEN'))