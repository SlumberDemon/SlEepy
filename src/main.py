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

@bot.command()
async def gl(ctx):
    for guild in bot.guilds:
        embed = discord.Embed(title=f'Guild-{guild.id}', description=f'` Name ` {guild} \n ` Members ` {guild.member_count}') 
        await ctx.send(embed=embed)

# Cogs

bot.load_extension('cogs.Slash')
bot.load_extension('cogs.Apps')
bot.load_extension('cogs.Events')
bot.load_extension('cogs.Error')

bot.run(getenv('TOKEN'))