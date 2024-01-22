import discord


async def embed(interakcia: discord.Interaction):
    
    emb = discord.Embed()

    await interakcia.channel.send(embed=emb)
    await interakcia.response.send_message("Embed bol úspešne skomponovaný a poslaný.", ephemeral=True)
