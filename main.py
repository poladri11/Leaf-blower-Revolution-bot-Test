from discord.ext import commands
from discord import app_commands
import discord
from typing import Optional
import typing
from typing import Literal
from discord.app_commands import Choice
import boss_info_embeds
import cards_information




guild = discord.Object(id=709522347383586897)


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)

intents = discord.Intents.default()
client = MyClient(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('-------------')






#Floor DMG calculator
@client.tree.command()
@app_commands.describe(
    floor='The floor of the pyramid you want to check',
)
async def floor(interaction: discord.Interaction, floor: int):
    """Floor DMG calculator!"""
    basedmg = 154000000000

    if floor > 987:
        await interaction.response.send_message("Sorry!\nThe bot can't handle numbers that high, so please, use a number equal or lower than 987", ephemeral=True)

    else:
        for x in range(floor):
            if x == 0:
                continue
            else:
                basedmg = basedmg*2

        await interaction.response.send_message("Damage needed for floor: **{}**\n**{:.2e} SlapDMG**".format(floor, basedmg), ephemeral=True)


#Bosses information
@client.tree.command()
@app_commands.describe(boss='Select the boss you want to see information about',)
@app_commands.choices(boss=boss_info_embeds.boss_choices)
async def boss_info(interaction: discord.Interaction, boss: str):
    """Sends a message with the information about the boss you selected"""
    boss_data = boss_info_embeds.boss_data
    for x in boss_data:

        if x['name'] == boss:

            await interaction.response.send_message(embed=boss_info_embeds.embed(x), ephemeral=True)






#Cards information
@client.tree.command()
@app_commands.describe(
    card='The card do you want to see information about', 
    tier='The tier of the card you want to see information about.'
)
@app_commands.choices(card=cards_information.cards_choices, tier=cards_information.cards_tiers)
async def card_info(interaction: discord.Interaction, card: str, tier: str):
    """Card stats looking"""
    
    embed_card = discord.Embed(colour=discord.Colour(0xc30cc1))
    cards_tier = cards_information.card_inf(tier)

    for x in cards_tier:
        if x['Name'] == card:

            for key, value in x.items():

                if key == 'thumbnail':
                    embed_card.set_thumbnail(url=value)

                else:
                    embed_card.add_field(name=key, value=value, inline=True)

    

    await interaction.response.send_message(embed=embed_card, ephemeral=True)


client.run('')
