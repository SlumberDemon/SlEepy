import discord, dislash
from dislash import slash_command
from discord.ext import commands

class Slash(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(description='Shows bot latency')
    async def latency(self, ctx):
        embed = discord.Embed(description=f'🏓 Pong! {round(self.bot.latency * 1000)}ms', colour=0xffa408)
        await ctx.send(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(Slash(bot))
