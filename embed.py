import discord


async def embed(interakcia: discord.Interaction):
    emb = discord.Embed()

    emb.set_author(name="Filip", icon_url="https://drive.google.com/uc?id=1ffbE0t7dY6NDVHgWuGpgQiN03eipXO2T")

    await interakcia.channel.send(embed=emb)
    await interakcia.response.send_message("Embed bol úspešne skomponovaný a poslaný.", ephemeral=True)
