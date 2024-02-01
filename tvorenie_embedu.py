import discord
from datetime import datetime

import databaza


async def run(interakcia: discord.Interaction):

    embed = discord.Embed(title="Need help?",
                          description="Seems like you need some assistance with some of my supported products. Or maybe you want to create a custom game from scratch and need a dev? Either way, you're in the right place.",
                          colour=0xf8f8f8)

    embed.set_author(name="Filip (filipeex) Karab",
                     icon_url="https://drive.google.com/uc?id=1ffbE0t7dY6NDVHgWuGpgQiN03eipXO2T")

    embed.add_field(name="How to get support?",
                    value="> `Well, it depends. You have 3 options. If you need to reach just me and no one else, you can either create a ticket, but most likely just DM me, or send me an email to filip@karab.sk. However if you need support from my mods or about anything else, here are your options:`",
                    inline=False)
    embed.add_field(name="Create a ticket.",
                    value="> `You can create a `<#1186241213158916166>` by clicking the create ticket button in the mentioned channel. A ticket is a private channel between you, me and my staff.`",
                    inline=True)
    embed.add_field(name="Join the drag-me room.",
                    value="> `In case you need immediate help with something and it can't wait, you can join the drag-me voice channel and me and the mods will get notified that you are requesting support, and we will try to get to you asap.`",
                    inline=True)
    embed.add_field(name="When can I get support?",
                    value="> `You can usually get support from around 4PM to 8PM every day, and from 9AM to about 9PM on the weekends. Mind you, sometimes it might take longer to receive support.`",
                    inline=False)

    embed.set_footer(text="Hope you have a great rest of your day - Filip :)")

    await interakcia.channel.send(embed=embed)
    await interakcia.response.send_message("Successfully sent the pre-programmed embed.", ephemeral=True)
