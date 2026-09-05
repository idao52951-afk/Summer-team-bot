import os
import asyncio
from highrise import BaseBot, Highrise, SessionMetadata

TOKEN = os.getenv("HIGHRISE_TOKEN")
ROOM_ID = os.getenv("ROOM_ID")

class Bot(BaseBot):
    async def on_start(self, session: SessionMetadata):
        print(f"Bot started! Connected to room: {session.room_id} ✅")
        await self.highrise.chat("Bot en ligne! 👋")

    async def on_chat(self, user, message: str):
        print(f"{user.username}: {message}")
        if message.lower() == "salut":
            await self.highrise.chat(f"Salut {user.username} 👋")

async def main():
    if not TOKEN or not ROOM_ID:
        print("ERROR: HIGHRISE_TOKEN or ROOM_ID missing")
        return
    await Highrise.run(TOKEN, ROOM_ID, [Bot()])

asyncio.run(main())
