from highrise import BaseBot
from highrise.models import SessionMetadata, User

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata):
        print(f"Bot connecté ! Room: {session_metadata.room_id}")
        await self.highrise.chat("Salut je suis en ligne ✅")

    async def on_chat(self, user: User, message: str):
        if message.startswith("!"):
            if message == "!ping":
                await self.highrise.chat(f"Pong {user.username} 🏓")
            if message == "!hello":
                await self.highrise.chat(f"Salut {user.username} 👋")
