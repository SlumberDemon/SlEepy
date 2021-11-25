import discord, dislash
from dislash import slash_command, SlashInteraction, ContextMenuInteraction
from discord.ext import commands

class Apps(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @dislash.user_command(name="Created at")
    async def created_at(self, inter: ContextMenuInteraction):
        await inter.respond(
            f"{inter.user} was created at {inter.user.created_at}",
            ephemeral=True 
        )

    @dislash.message_command(name="Reverse")
    async def reverse(self, inter: ContextMenuInteraction):
        if inter.message.content:
            await inter.respond(inter.message.content[::-1])
        else:
            await inter.respond("There's no content", ephemeral=True)

    @dislash.message_command(name="Quote")
    async def quote(self, inter: ContextMenuInteraction):
        embed = discord.Embed(description=inter.message.content)
        embed.set_author(name=f'{inter.author}', icon_url=inter.author.avatar.url)
        await inter.respond(embed=embed)

def setup(bot):
    bot.add_cog(Apps(bot))
