import discord


async def clear(interakcia: discord.Interaction, sprav: int = None):
    if str(interakcia.user) != "filipeex_":
        await interakcia.response.send_message("You don't have permission to do that!", ephemeral=True)
        return
    if sprav:
        if sprav <= 0 or sprav > 100:
            await interakcia.response.send_message("Invalid amount of messages, can be anywhere from 1 to 100.",
                                                   ephemeral=True)
            return
    if sprav:
        await interakcia.response.send_message(f"Successfully removed {sprav} messages, it might take a while to see the effect, give it a minute.", ephemeral=True)
    else:
        await interakcia.response.send_message(f"Successfully removed all the messages, it might take a while to see the effect, give it a minute.", ephemeral=True)
    if sprav:
        await interakcia.channel.purge(limit=sprav)
    else:
        await interakcia.channel.purge()
