import discord, dislash, datetime
from dislash import slash_command, SlashInteraction, ContextMenuInteraction
from discord.ext import commands
from src.extras.views import url_button_generator

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
        view = url_button_generator(label='View message', url=inter.message.jump_url)
        embed = discord.Embed(description=inter.message.content, timestamp=inter.message.datetime())
        embed.set_author(name=f'{inter.message.author}', icon_url=inter.message.author.avatar.url)
        await inter.respond(embed=embed, view=view)

def setup(bot):
    bot.add_cog(Apps(bot))
