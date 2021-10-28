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

    @slash_command(description='Bot invite')
    async def invite(self, ctx):
        embed = discord.Embed(description='[invite](https://discord.com/api/oauth2/authorize?client_id=903187756254130177&permissions=3557156934&scope=applications.commands%20bot)')
        await ctx.send(embed=embed, ephemeral=True)

    @slash_command(description='Shows info on the developer')
    async def slumberdemon(self, ctx):
        embed = discord.Embed(title='SlumberDemon', description='Professional Sleepy Head \n and B.O.A.T Developer', colour=0xecdbd9)
        embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/549563196579774465/f1df0e07a490bfbeb4704a54d6181fd8.webp?size=1024')
        embed.add_field(name='Website', value='[click here](https://slumberdemon.carrd.co/)')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Slash(bot))
