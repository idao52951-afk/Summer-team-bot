import asyncio
from highrise import BaseBot
from highrise.__main__ import main

BOT_TOKEN = 5ff2d317c2efd26d3005ee486fb658768d869d075df57774ebabd98a98bac17b
ROOM_ID = https://high.rs/world?id=6894bd39e3e4a405517cb530&ownedRoomId=6a95a3ab0cfd91711d40d5d6&invite_id=6a986f31259f48a4c29ed5cd

class Bot(BaseBot):
    async def on_start(self):
        await self.highrise.chat("Bot du lycée connecté ✅ Tape !help")

    async def on_chat(self, user, message):
        if message.lower() == "!help":
            await self.highrise.chat("Commandes: !help | !dance | !vip")
        if message.lower() == "!dance":
            await self.highrise.send_emote("dance-tiktok8", user.id)

asyncio.run(main(Bot(), BOT_TOKEN, ROOM_ID))
