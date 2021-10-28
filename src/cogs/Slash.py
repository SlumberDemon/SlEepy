import discord, dislash
from dislash import slash_command
from discord.ext import commands

guilds = [877399405056102431, 819112190115446844]

class Slash(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(description='Shows bot latency', guild_ids=guilds)
    async def latency(self, ctx):
        embed = discord.Embed(description=f'🏓 Pong! {round(self.bot.latency * 1000)}ms', colour=0xffa408)
        await ctx.send(embed=embed, ephemeral=True)

    @slash_command(description='Bot invite', guild_ids=guilds)
    async def invite(self, ctx):
        embed = discord.Embed=(description=f'[invite](https://discord.com/api/oauth2/authorize?client_id=903187756254130177&permissions=3557156934&scope=applications.commands%20bot)')
        await ctx.send(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(Slash(bot))
