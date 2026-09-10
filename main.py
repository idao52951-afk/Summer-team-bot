import os
import asyncio
from highrise import __main__

# On récupère les variables de Railway
TOKEN = os.getenv("HIGHRISE_TOKEN")
ROOM_ID = os.getenv("ROOM_ID")

if __name__ == "__main__":
    # format: "fichier:Classe", ROOM_ID, TOKEN
    __main__.run(("bot:Bot", ROOM_ID, TOKEN))
