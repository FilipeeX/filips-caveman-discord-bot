import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def token():
    return os.environ.get("TOKEN")


def databaza_ip():
    return os.environ.get("IP")


def databaza_port():
    return os.environ.get("PORT")


def databaza_user():
    return os.environ.get("POUZIVATEL")


def databaza_heslo():
    return os.environ.get("HESLO")


def databaza():
    return os.environ.get("DATABAZA")
