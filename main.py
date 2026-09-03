import asyncio
import os
from highrise import BaseBot, User, AnchorPosition, Position, Reaction, ChatEvent
from highrise.__main__ import main

DANCES = {
    "cozynap": "dance-cute",
    "dance": "dance-tiktok8",
    "wave": "emote-wave"
}

VIP_USERS = set()

class Bot(BaseBot):
    async def on_start(self):
        print("Bot connecté!")
        await self.highrise.chat("Bot est en ligne ✅")

    async def on_user_join(self, user: User):
        await self.highrise.chat(f"Bienvenue @{user.username} dans la room ❤️😍! Soyez respectueux et amusez-vous bien!")

    async def on_chat(self, user: User, message: str):
        msg = message.lower()
        if msg == "stop":
            await self.highrise.walk_to(Position(0, 0, 0))
            await self.highrise.chat("Animation arrêtée ✅")
            return
        if msg.startswith("!"):
            cmd = msg[1:]
            if cmd in DANCES:
                await self.highrise.send_emote(DANCES[cmd], user.id)
                await self.highrise.chat(f"Vous bouclez [{cmd}]! Tapez 'Stop' pour arrêter.")
                return
        if msg == "!vip":
            await self.highrise.chat("Envie de profiter du VIP? Envoyez 500g au bot!")
        if msg == "!help":
            await self.highrise.chat("Commandes:!dance,!cozynap,!wave,!vip,!help. Tape Stop pour arrêter.")

    async def on_tip(self, sender: User, receiver: User, tip):
        if receiver.id == self.bot_user.id and tip.amount >= 500:
            VIP_USERS.add(sender.id)
            await self.highrise.chat(f"Merci @{sender.username} pour le VIP 👑 Tu as accès aux zones VIP maintenant!")

if __name__ == "__main__":
    asyncio.run(main(Bot()))
