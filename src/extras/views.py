import discord
from discord.ext import commands


class Help_Dropdown(discord.ui.Select):
    def __init__(self, context: commands.Context):
        self.ctx = context

        options = [
            discord.SelectOption(label='Utility', description='Utility Commands', value='0'),
            discord.SelectOption(label='Moderation', description='Moderation Commands', value='1')
        ]

        super().__init__(placeholder='Select Help Page', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if interaction.user == self.ctx.author:
            if int(self.values[0]) == 0:
                Utility = discord.Embed(title='Utility', colour=0xc3d9df)
                Utility.add_field(name='**latency**', value='Shows bot latency', inline=False)
                Utility.add_field(name='**Invite**', value='Bot Invite', inline=False)
                Utility.add_field(name='**SlumberDemon**', value='Shows info on the developer', inline=False)
                await interaction.response.edit_message(embed=Utility)
            elif int(self.values[0]) == 1:
                Mod = discord.Embed(title='Moderation', colour=0xc3d9df)
                Mod.add_field(name='**Ban**', value='Ban user', inline=False)
                Mod.add_field(name='**Kick**', value='Kick user', inline=False)
                Mod.add_field(name='**Embed**', value='Create embeds', inline=False)
                await interaction.response.edit_message(embed=Mod)
            else:
                await interaction.response.send_message('Embed error', ephemeral=True)
        else:
            await interaction.response.send_message('You are not allowed to control this message', ephemeral=True)

class Dropdown_Help_Send(discord.ui.View):
    def __init__(self, ctx: commands.Context):
        super().__init__()

        url1 = f'https://discord.com/api/oauth2/authorize?client_id=903187756254130177&permissions=3557156934&scope=applications.commands%20bot'

        self.ctx = ctx

        self.add_item(Help_Dropdown(ctx))
        self.add_item(discord.ui.Button(label='Invite', url=url1))

class invite_link(discord.ui.View):
    def __init__(self):
        super().__init__()

        url1 = f'https://discord.com/api/oauth2/authorize?client_id=903187756254130177&permissions=3557156934&scope=applications.commands%20bot'

        self.add_item(discord.ui.Button(label='Invite', url=url1))
