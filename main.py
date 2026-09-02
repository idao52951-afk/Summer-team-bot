import highrise
from highrise import BaseBot

BOT_TOKEN = "f38c6c63c0b03e572c699981d0cbbc664c3f7a89f7fec5182189a5a1077027bf"
ROOM_ID = "6a95a3ab0cfd91711d40d5d6"

class Bot(BaseBot):
    async def on_start(self, session):
        print("Bot Summer Team connecté !")
        await self.highrise.chat("Salut tout le monde, Summer Team est là 😎")

bot = Bot()
highrise.run(bot, BOT_TOKEN, ROOM_ID)
