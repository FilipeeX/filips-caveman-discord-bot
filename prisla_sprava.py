import discord
from discord.utils import get


verif_kanal_id = 1186004159699357697
verif_role_ids = [
    1185727822908625017,
    1185730792970780692,
    1185727514715373598,
    1185731353359159406
]
welcome_kanal_id = 1186018809543393412


async def run(sprava: discord.Message):
    kanal = sprava.channel

    if je_verif_kanal(kanal):
        await verifikacia(sprava)
        return


async def verifikacia(sprava: discord.Message):
    pouzivatel = sprava.author
    server = sprava.guild

    text = sprava.content
    if spravna_sprava(text):

        role = await ids_na_role(verif_role_ids, server)
        await pouzivatel.add_roles(
            role[0],
            role[1],
            role[2],
            role[3],
            reason="Verification"
        )

        await welcome_sprava(pouzivatel, server)

    await sprava.delete()


async def welcome_sprava(pouzivatel: discord.User, server: discord.Guild):

    kanal = get(server.text_channels, id=welcome_kanal_id)
    embed = discord.Embed(
        title=f"Welcome in the cave! :tada:",
        description=f"<@{pouzivatel.id}>",
        color=0x404040
    )

    await kanal.send(embed=embed)


async def ids_na_role(ids: list[int], server: discord.Guild):
    vysledok = []
    [vysledok.append(get(server.roles, id=i)) for i in ids]
    return vysledok


def je_verif_kanal(kanal: discord.TextChannel):
    return str(kanal.id) == str(verif_kanal_id)


def spravna_sprava(text: str):
    spravna = "you know the rules, and so do i."
    return je_podobny(text.lower(), spravna)


def je_podobny(str1, str2):
    str1 = str1 + ' ' * (len(str2) - len(str1))
    str2 = str2 + ' ' * (len(str1) - len(str2))

    prob = sum(1 if i == j else 0
               for i, j in zip(str1, str2)) / float(len(str1))
    return prob > .5
