import discord, dislash
from dislash import slash_command
from discord.ext import commands


class Slash(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Utility

    @slash_command(description='Shows bot latency')
    async def latency(self, ctx):
        embed = discord.Embed(description=f'🏓 Pong! {round(self.bot.latency * 1000)}ms', colour=0xc3d9df)
        await ctx.send(embed=embed)

    @slash_command(description='Bot invite')
    async def invite(self, ctx):
        embed = discord.Embed(description='[invite](https://discord.com/api/oauth2/authorize?client_id=903187756254130177&permissions=3557156934&scope=applications.commands%20bot)', colour=0xc3d9df)
        await ctx.send(embed=embed)

    @slash_command(description='Shows info on the developer')
    async def slumberdemon(self, ctx):
        embed = discord.Embed(title='SlumberDemon', description='Professional Sleepy Head \n and B.O.A.T Developer', colour=0xc3d9df)
        embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/549563196579774465/f1df0e07a490bfbeb4704a54d6181fd8.webp?size=1024')
        embed.add_field(name='Website', value='[click here](https://slumberdemon.carrd.co/)')
        await ctx.send(embed=embed)
    
    # Mod

    @slash_command(description='Ban user')
    @dislash.has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.Member, *, reason=None):
        await member.ban(reason=reason)
        icon = member.avatar.url
        embed = discord.Embed(description=f'Reason: `{reason}`', colour=0xc3d9df)
        embed.set_author(name=f'{member} has been kicked', icon_url=icon)
        await ctx.send(embed=embed)

    @slash_command(description='Kick user')
    @dislash.has_permissions(kick_members=True)
    async def ban(self, ctx, member:discord.Member, *, reason=None):
        await member.kick(reason=reason)
        icon = member.avatar.url
        embed = discord.Embed(description=f'Reason: `{reason}`', colour=0xc3d9df)
        embed.set_author(name=f'{member} has been kicked', icon_url=icon)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Slash(bot))
