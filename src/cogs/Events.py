import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='-help'))
        print('Logged in as ---->', self.bot.user)

def setup(bot):
    bot.add_cog(Events(bot))