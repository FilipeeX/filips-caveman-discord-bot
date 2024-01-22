import discord
from discord import app_commands

import clear
import pv
import sync
import embed


intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


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
    await embed.embed(interakcia)



@client.event
async def on_ready():
    print(f'Úspešne prihlásenie za {client.user}.')


token = pv.token()
client.run(token)