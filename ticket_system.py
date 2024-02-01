import discord

import databaza
import tvorenie_embedu

from discord.utils import get


ticket_tvorba_kanal_id = 1186241213158916166
ticket_tvorba_sprava_id = 1202211822317600780
kategoria_id = 1185952412876415016


class TicketView(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="Close", style=discord.ButtonStyle.red, emoji='📑')
    async def _button(self, interakcia: discord.Interaction, tlacitko: discord.Button):

        kanal_id = interakcia.channel.id
        sprava_id = interakcia.message.id

        await interakcia.channel.delete()
        databaza.odstran_ticket(kanal_id, sprava_id)


class TicketTvorbaView(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="Create a Ticket", style=discord.ButtonStyle.blurple, emoji='📩')
    async def _button(self, interakcia: discord.Interaction, tlacitko: discord.Button):

        server = interakcia.guild
        kategoria = get(server.categories, id=kategoria_id)
        pouzivatel = interakcia.user

        if databaza.ma_uz_ticket(pouzivatel):
            await interakcia.response.send_message("You already have a ticket created.", ephemeral=True)
            return

        kanal = await kategoria.create_text_channel(f"🧻╰{pouzivatel}")

        # TODO pridat perms role staff perms

        embed = ticket_sprava_embed()
        sprava = await kanal.send(embed=embed,
                                  view=TicketView())

        databaza.novy_ticket(kanal.id, sprava.id, interakcia.user)

        await interakcia.response.send_message(f"Your ticket has been created, <#{kanal.id}>.", ephemeral=True)


async def nacitaj_tlacitka(server: discord.Guild):

    kanal = get(server.text_channels, id=ticket_tvorba_kanal_id)
    sprava = await kanal.fetch_message(ticket_tvorba_sprava_id)

    await sprava.edit(content=sprava.content, embed=sprava.embeds[0], view=TicketTvorbaView())

    ids_tlacitok = databaza.tickety()
    for kanal_id in ids_tlacitok:

        kanal = get(server.text_channels, id=int(kanal_id))
        sprava = await kanal.fetch_message(ids_tlacitok[kanal_id])

        await sprava.edit(content=sprava.content, embed=sprava.embeds[0], view=TicketView())


def ticket_sprava_embed():
    embed = discord.Embed(title="Welcome to your ticket!",
                          description="This is a private place where you can talk to my mods or me, you can discuss offers, potential clients or anyting really because no information leaves this channel.",
                          colour=0x3641be)

    embed.set_author(name="Filip (filipeex) Karab",
                     icon_url="https://drive.google.com/uc?id=1ffbE0t7dY6NDVHgWuGpgQiN03eipXO2T")

    embed.add_field(name="Who are you?",
                    value="> `Hi! My name is Filip and I am a freelance developer. I develop many different things, anything from minecraft plugins to games really. If you would like to find out more about me, you can here: `<#1186240258443051039>`.`",
                    inline=True)
    embed.add_field(name="What can I do in a ticket?",
                    value="> `You have created a ticket, also known as this channel. Here, you can connect with me, or my mods and really talk from your soul. Anything you need from me releated to business, development or support you can ask here.`",
                    inline=True)

    embed.set_footer(text="Hope you have a great rest of your day - Filip :)")

    return embed