import discord
from datetime import datetime

import databaza


async def run(interakcia: discord.Interaction):

    emb = discord.Embed(title="Send *'You know the rules, and so do I.'* here, to verify yourself!",
                        description="Verify yourself by rewriting the phrase \"You know the rules, and so do I.\", and then send it in here.",
                        colour=0xfa301e)

    emb.set_author(name="Filip (filipeex) Karab",
                   icon_url="https://drive.google.com/uc?id=1ffbE0t7dY6NDVHgWuGpgQiN03eipXO2T")

    emb.add_field(name="Verification, why?",
                  value="> `So we know you're not some kind of a bot, and also by verifying, you agree to follow the rules of this server.`",
                  inline=False,
                  )
    emb.add_field(name="Isn't there a better way to do this?",
                  value="> `Of course, discord itself has a few options for rule agreement before joining a server, but this is way better. Not only do i get to rickroll you, this way I can also show off what can my discord bots do.`",
                  inline=False)

    emb.set_footer(text="Hope you have a great day - Filip :)")

    await interakcia.channel.send(embed=emb)
    await interakcia.response.send_message("Successfully sent the pre-programmed embed.", ephemeral=True)