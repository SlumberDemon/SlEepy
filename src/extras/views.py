import discord
from discord.ext import commands

class invite_link(discord.ui.View):
    def __init__(self):
        super().__init__()

        url1 = f'https://discord.com/api/oauth2/authorize?client_id=903187756254130177&permissions=3557156934&scope=applications.commands%20bot'

        self.add_item(discord.ui.Button(label='Invite', url=url1))
