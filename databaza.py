import discord
import mysql.connector
import pv


konfiguracia = {
    'user': pv.databaza_user(),
    'password': pv.databaza_heslo(),
    'host': pv.databaza_ip(),
    'port': pv.databaza_port(),
    'database': pv.databaza()
}


def tickety():
    v = {}

    napojenie = mysql.connector.connect(**konfiguracia)
    kurzor = napojenie.cursor()

    kurzor.execute("SELECT * FROM tickety;")
    riadky = kurzor.fetchall()

    for riadok in riadky:
        v[riadok[2]] = riadok[3]

    kurzor.close()
    napojenie.close()

    return v


def ma_uz_ticket(pouzivatel: discord.User):

    napojenie = mysql.connector.connect(**konfiguracia)
    kurzor = napojenie.cursor()

    kurzor.execute(f"SELECT * FROM tickety WHERE autor_meno = '{pouzivatel}' AND autor_id = '{pouzivatel.id}';")
    kurzor.fetchall()
    res = kurzor.rowcount

    kurzor.close()
    napojenie.close()

    return res > 0


def novy_ticket(id_kanalu: int, id_ticketu: int, autor: discord.User):

    napojenie = mysql.connector.connect(**konfiguracia)
    kurzor = napojenie.cursor()

    kurzor.execute(f"INSERT INTO tickety (autor_meno, autor_id, kanal_id, sprava_id) VALUES ('{autor}', '{autor.id}', '{id_kanalu}', '{id_ticketu}');")
    napojenie.commit()

    kurzor.close()
    napojenie.close()


def odstran_ticket(id_kanalu: int, id_ticketu: int):

    napojenie = mysql.connector.connect(**konfiguracia)
    kurzor = napojenie.cursor()

    kurzor.execute(f"DELETE FROM tickety WHERE kanal_id = '{id_kanalu}' AND sprava_id = '{id_ticketu}';")
    napojenie.commit()

    kurzor.close()
    napojenie.close()
