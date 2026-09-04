import os
import asyncio
from highrise import BaseBot
from highrise.__main__ import main
from highrise import BaseBot, Position

BOT_TOKEN = os.getenv("BOT_TOKEN")
ROOM_ID = "6894bd39e3e4a405517cb530"  # L'ID de la room

class Bot(BaseBot):
    async def on_start(self, session_metadata):
        await self.highrise.chat("Bot du lycée connecté ✅ Tape !help")

    async def on_chat(self, user, message):
        msg = message.lower()
        
        if msg == "!help":
            await self.highrise.chat("Commandes: !help | !dance | !vip")
        
        if msg == "!dance":
            await self.highrise.send_emote("dance-tiktok8", user.id)
        
        if msg == "!vip":
            await self.highrise.chat(f"{user.username} est VIP 👑")

main(BOT_TOKEN, ROOM_ID)
