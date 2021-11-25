import discord, dislash
from dislash import slash_command, SlashInteraction, ContextMenuInteraction
from discord.ext import commands

class Apps(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @dislash.user_command(name="Created at")
    async def created_at(self, inter: ContextMenuInteraction):
        # User commands always have only this ^ argument
        await inter.respond(
            f"{inter.user} was created at {inter.user.created_at}",
            ephemeral=True # Make the message visible only to the author
        )

    @dislash.message_command(name="Reverse")
    async def reverse(inter: ContextMenuInteraction):
        # Message commands always have only this ^ argument
        if inter.message.content:
            # Here we will send a reversed message to the chat
            await inter.respond(inter.message.content[::-1])
        else:
            # Here we will explain that the message isn't valid
            await inter.respond("There's no content", ephemeral=True)

def setup(bot):
    bot.add_cog(Apps(bot))
