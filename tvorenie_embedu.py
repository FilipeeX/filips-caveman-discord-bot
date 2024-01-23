import discord
from datetime import datetime


async def run(interakcia: discord.Interaction):

    embed = discord.Embed()

    await interakcia.channel.send(embed=embed)
    await interakcia.response.send_message("Successfully sent the pre-programmed embed.", ephemeral=True)
