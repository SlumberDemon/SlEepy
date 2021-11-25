import discord, dislash
from dislash import slash_command, SlashInteraction, ContextMenuInteraction
from discord.ext import commands

class App(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @dislash.user_command(name="Created at")
    async def created_at(self, inter: ContextMenuInteraction):
        # User commands always have only this ^ argument
        await inter.respond(
            f"{inter.user} was created at {inter.user.created_at}",
            ephemeral=True # Make the message visible only to the author
        )

def setup(bot):
    bot.add_cog(App(bot))
