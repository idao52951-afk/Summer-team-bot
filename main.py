import os
import asyncio
from highrise import BaseBot, Highrise, __main__
from highrise.models import SessionMetadata, User, AnchorPosition, Reaction, ChatEvent

# On récupère les variables de Railway
TOKEN = os.getenv("HIGHRISE_TOKEN")
ROOM_ID = os.getenv("ROOM_ID")

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata):
        print(f"Bot connecté ! Room: {session_metadata.room_id}")
