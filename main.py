import os
import asyncio
from highrise import BaseBot
from highrise.__main__ import main

BOT_TOKEN = os.getenv("BOT_TOKEN")
ROOM_ID = "6a95a3ab0cfd91711d40d5d6"

class Bot(BaseBot):
    async def on_start(self):
        await self.highrise.chat("Bot du lycée connecté ✅ Tape !help")

    async def on_chat(self, user, message):
        msg = message.lower()
        
        if msg == "!help":
            await self.highrise.chat("Commandes: !help | !dance | !vip")
        
        if msg == "!dance":
            await self.highrise.send_emote("dance-tiktok8", user.id)
        
        if msg == "!vip":
            await self.highrise.chat(f"{user.username} tu es VIP 👑")

asyncio.run(main(Bot(), BOT_TOKEN, ROOM_ID))
