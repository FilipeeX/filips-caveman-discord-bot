import discord
from discord.utils import get

cakarna_id = 1186241447771525170
notif_kanal_id = 1186243819193245826
ticket_kanal_id = 1186241213158916166

mod_rola_id = 1185728781168693258


async def run(pouzivatel: discord.Member, predtym: discord.VoiceState, potom: discord.VoiceState):

    if potom.channel is not None:
        if napojenie_cakarne(potom.channel, cakarna_id):
            dm = await pouzivatel.create_dm()
            await dm.send(f"> Thank you for using direct vc support, the staff team has been notified about your request and we'll try to get to you asap. However, it might take some time so it might be better to just create a <#{ticket_kanal_id}>.")

            kanal = najdi_kanal(notif_kanal_id, pouzivatel.guild)
            await kanal.send(f"<@{pouzivatel.id}> has joined the *drag me* channel, go help him out! <@&{mod_rola_id}>")


def napojenie_cakarne(kanal: discord.VoiceChannel, id_cakarne: int):
    return str(kanal.id) == str(id_cakarne)


def najdi_kanal(id_kanalu: int, server: discord.Guild):
    return get(server.text_channels, id=id_kanalu)
