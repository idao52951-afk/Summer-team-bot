import highrise
from highrise import BaseBot

BOT_TOKEN = "5ff2d317c2efd26d3005ee486fb658768d869d075df57774ebabd98a98bac17b"
ROOM_ID = "6a95a3ab0cfd91711d40d5d6"

class Bot(BaseBot):
    async def on_start(self, session):
        print("Bot Summer Team connecté !")
        await self.highrise.chat("Salut tout le monde, Summer Team est là 😎")

bot = Bot()
highrise.run(bot, BOT_TOKEN, ROOM_ID)
