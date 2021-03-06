import discord, dislash, asyncio, random, sys, datetime
from dislash import slash_command, SlashInteraction
from discord.ext import commands
from src.extras.views import invite_link, Dropdown_Help_Send, url_button_generator

class Slash(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Utility

    @slash_command(description='Help command')
    async def help(self, ctx):
        view = Dropdown_Help_Send(ctx)
        embed = discord.Embed(description='**Bot Help** \n Hello! Welcome to the help page. \n ** ** \n Use \"/help\" for this view. \n Use the dropdown menu below to select a category. \n **Support Server** \n For more help, consider joining the official server over at https://discord.gg/sQxptgyAu8 \n ** ** \n I\'m also open source. You can see my code on [GitHub](https://github.com/SlumberDemon/SlEepy/tree/main)!', colour=0xc3d9df)
        await ctx.send(embed=embed, view=view)

    @slash_command(description='Shows bot latency')
    async def latency(self, ctx):
        embed = discord.Embed(description=f'🏓 Pong! {round(self.bot.latency * 1000)}ms', colour=0xc3d9df)
        await ctx.send(embed=embed)

    @slash_command(description='Bot invite')
    async def invite(self, ctx):
        embed = discord.Embed(description='Bot invite', colour=0xc3d9df)
        await ctx.send(embed=embed, view=invite_link())

    @slash_command(description='Shows info on the developer')
    async def slumberdemon(self, ctx):
        embed = discord.Embed(title='SlumberDemon', description='Professional Sleepy Head \n and B.O.A.T Developer', colour=0xc3d9df)
        embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/549563196579774465/f1df0e07a490bfbeb4704a54d6181fd8.webp?size=1024')
        embed.add_field(name='Website', value='[click here](https://slumberdemon.carrd.co/)')
        await ctx.send(embed=embed)

    @slash_command(description='Shows user info')
    async def user(self, ctx, user:discord.User=None):
        user = ctx.author if not user else user
        embed = discord.Embed(title=f'{user}', description=f'` User ID ` {user.id} \n ** ** \n ` Account Created ` {user.created_at.strftime("%c")}', colour=0xc3d9df)
        embed.set_thumbnail(url=user.avatar.url)
        await ctx.send(embed=embed)

    @slash_command(description='Shows user avatar')
    async def avatar(self, ctx, user:discord.User=None):
        user = ctx.author if not user else user
        embed = discord.Embed(title=f'{user}', colour=0xc3d9df)
        embed.set_image(url=user.avatar.url)
        await ctx.send(embed=embed)

    @slash_command(description='Show bot source')
    async def source(self, ctx):
        embed = discord.Embed(title='SlEepy Source', colour=0xc3d9df)
        view = url_button_generator(label='Source', url='https://github.com/SlumberDemon/SlEepy/tree/main')
        await ctx.send(embed=embed, view=view)

    @slash_command(description='Shows bot info')
    async def info(self, ctx):
        embed = discord.Embed(title='Bot info', colour=0xc3d9df)
        embed.add_field(name='Guild count', value=f'`{len(self.bot.guilds)}`')
        await ctx.send(embed=embed)

    # Mod

    @slash_command(description='Ban user')
    @dislash.has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.Member, *, reason=None):
        await member.ban(reason=reason)
        icon = member.avatar.url
        embed = discord.Embed(description=f'Reason: `{reason}`', colour=0xc3d9df)
        embed.set_author(name=f'{member} banned', icon_url=icon)
        await ctx.send(embed=embed)

    @slash_command(description='Kick user')
    @dislash.has_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.Member, *, reason=None):
        await member.kick(reason=reason)
        icon = member.avatar.url
        embed = discord.Embed(description=f'Reason: `{reason}`', colour=0xc3d9df)
        embed.set_author(name=f'{member} kicked', icon_url=icon)
        await ctx.send(embed=embed)

    @slash_command(description='Unban user')
    @dislash.has_permissions(ban_members=True)
    async def unban(self, ctx, member):
        embed = discord.Embed()
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        
        for ban_entery in banned_users:
            user = ban_entery.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed.set_author(name=f'{user.name}#{user.discriminator} Unbanned', icon_url=user.avatar.url)
                await ctx.send(embed=embed)
                return

    @slash_command(description='Create embeds')
    @dislash.has_permissions(manage_messages=True)
    async def embed(self, ctx, title=None, description=None, color=None, image=None, footer=None):
        if color is not None:
            try:
                color = await commands.ColorConverter().convert(self, color)
            except:
                color = None
        if color is None:
            color = discord.Color.default()
        emb = discord.Embed(color=color)
        if title is not None:
            emb.title = title
        if description is not None:
            emb.description = description
        if image is not None:
            emb.set_image(url=image)
        if footer is not None:
            emb.set_footer(text=footer)
        await ctx.send(embed=emb)
    
    @slash_command(description='Giveaway command')
    async def giveaway(self, ctx, time, prize):
        time_convert = {'s':1, 'm':60, 'h':3600, 'd': 86400}
        ctime = int(time[0]) * time_convert[time[-1]]
        embed1 = discord.Embed(title=prize, description=f'React with 🎉 to enter \n Time remaining: {ctime}s', colour=0xc3d9df)
        msg = await ctx.send(embed=embed1)

        await msg.add_reaction('🎉')
        await asyncio.sleep(ctime)

        new_msg = await ctx.channel.fetch_message(msg.id)

        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))

        winner = random.choice(users)

        view = url_button_generator(label='Jump to original message', url=msg.jump_url)
        embed2 = discord.Embed(title=prize, description=f'Winner: {winner.mention} \n Hosted by: {ctx.author.mention}', timestamp=datetime.datetime.utcnow())
        embed2.set_footer(text='Ended at ')
        await msg.edit('🎉 **GIVEAWAY ENDED** 🎉', embed=embed2)
        await ctx.send(f'Congratulations {winner.mention}! You won the **{prize}**!', view=view)
        
def setup(bot):
    bot.add_cog(Slash(bot))
