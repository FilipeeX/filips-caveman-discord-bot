import discord
from discord import app_commands


async def sync(interakcia: discord.Interaction, tree: app_commands.CommandTree):
    if str(interakcia.user) != "filipeex_":
        await interakcia.response.send_message(f"You don't have permission to do that!", ephemeral=True)
        return
    await tree.sync()
    await interakcia.response.send_message("Successfully synced the command tree of the bot.", ephemeral=True)
