import discord, dislash
from discord.ext import commands
from src.extras.emojis import Emo

class Listener(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        channel = 903926683185348619
        await channel.send(error)
        
    @commands.Cog.listener()
    async def on_slash_command_error(self, inter, error):
        channel = 903926683185348619
        await channel.send(error)


def setup(bot):
    bot.add_cog(Listener(bot))
