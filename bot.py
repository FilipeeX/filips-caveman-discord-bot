import socket
import discord
import mysql.connector.errors
from discord import app_commands

import clear
import databaza
import prisla_sprava
import pv
import sync
import ticket_system
import tvorenie_embedu
import voice_zmena


intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

server_id = 1185588092560736356


@tree.command(
    name="sync",
    description="An admin only command that synchronizes the command tree of the bot."
)
async def _sync(interakcia: discord.Interaction):
    await sync.sync(interakcia, tree)


@tree.command(
    name="clear",
    description="Remove a specified amount of messages from the current channel."
)
@app_commands.describe(sprav="Number of messages to remove.")
@app_commands.rename(sprav="amount")
async def _clear(interakcia: discord.Interaction, sprav: int = None):
    await clear.clear(interakcia, sprav)


@tree.command(
    name="embed",
    description="An admin only command, sends a pre-made embed from the code."
)
async def _embed(interakcia: discord.Interaction):
    await tvorenie_embedu.run(interakcia)


@client.event
async def on_message(sprava: discord.Message):
    await prisla_sprava.run(sprava)


@client.event
async def on_voice_state_update(pouzivatel: discord.Member, predtym: discord.VoiceState, potom: discord.VoiceState):
    await voice_zmena.run(pouzivatel, predtym, potom)


@client.event
async def on_ready():
    print(f'Successfully logged in as {client.user}.')
    await ticket_system.nacitaj_tlacitka(client.get_guild(server_id))
    print(f'MySQL connection established successfully.')


token = pv.token()
client.run(token)
