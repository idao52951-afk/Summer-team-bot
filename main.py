import zipfile
import sys
import os

# 1. Dézippe le SDK d'abord
if not os.path.exists('./python-bot-sdk-main'):
    print("Extracting SDK...")
    with zipfile.ZipFile('python-bot-sdk-main.zip', 'r') as zip_ref:
        zip_ref.extractall('.')

# 2. Ajoute le dossier au path
sys.path.append('./python-bot-sdk-main')

# 3. Maintenant on importe
from highrise import BaseBot, Highrise
import asyncio

# 4. TON CODE DE BOT VIENT ICI
# Exemple basique:
class Bot(BaseBot):
    async def on_start(self, session):
        print("Bot started!")

if __name__ == "__main__":
    # Mets ton token ici
    token = os.getenv("HIGHRISE_TOKEN")
    room_id = os.getenv("ROOM_ID")
    
    highrise = Highrise(token, room_id)
    bot = Bot()
    asyncio.run(highrise.run(bot))
