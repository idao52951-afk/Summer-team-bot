import os
import asyncio
from highrise import BaseBot, User, Anchor, SessionMetadata
from highrise.__main__ import main

TOKEN = os.getenv("HIGHRISE_TOKEN")
ROOM_ID = os.getenv("ROOM_ID")

class Bot(BaseBot):
    async def on_start(self, session: SessionMetadata):
        print(f"Bot démarré dans la room: {session.room_id}")

    async def on_user_join(self, user: User, position: Anchor):
        await self.highrise.chat(f"Bienvenue {user.username} dans la room ! 👋")

    async def on_chat(self, user: User, message: str):
        if message.lower() == "!help":
            await self.highrise.chat(f"{user.username} → Commandes: !help, !ping")
        
