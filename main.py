import zipfile
import sys
import os
import asyncio
import glob

# 1. Dézippe le SDK au démarrage
if not os.path.exists('./python-bot-sdk-main'):
    print("Extracting SDK...")
    with zipfile.ZipFile('python-bot-sdk-main.zip', 'r') as zip_ref:
        zip_ref.extractall('.')
    print("SDK Extracted!")

# 2. TROUVE AUTOMATIQUEMENT LE DOSSIER QUI CONTIENT "highrise"
sdk_paths = glob.glob('./python-bot-sdk-main/**/highrise', recursive=True)
if sdk_paths:
    sdk_folder = os.path.dirname(sdk_paths[0])
    print(f"Found SDK at: {sdk_folder}")
    sys.path.append(sdk_folder)
else:
    print("ERROR: Could not find highrise folder")

# 3. Import du SDK Highrise
from highrise import BaseBot, Highrise

# 4. TON BOT ICI
class Bot(BaseBot):
    async def on_start(self, session):
        print("Bot started! Connected to Highrise ✅")

    async def on_chat(self, user, message):
        print(f"{user.username}: {message}")
        if message.lower() == "salut":
            await self.highrise.chat(f"Salut {user.username} 👋")

if __name__ == "__main__":
    token = os.getenv("HIGHRISE_TOKEN")
    room_id = os.getenv("ROOM_ID")

    if not token or not room_id:
        print("ERROR: HIGHRISE_TOKEN or ROOM_ID missing in Environment")
        exit(1)

    highrise = Highrise(token, room_id)
    bot = Bot()
    asyncio.run(highrise.run(bot))
