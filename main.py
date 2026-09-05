import zipfile
import sys
import os
import asyncio
import glob
import websockets
import json

# 1. Dézippe le SDK
if not os.path.exists('./python-bot-sdk-main'):
    print("Extracting SDK...")
    with zipfile.ZipFile('python-bot-sdk-main.zip', 'r') as zip_ref:
        zip_ref.extractall('.')
    print("SDK Extracted!")

# 2. Trouve le dossier SDK
sdk_paths = glob.glob('./python-bot-sdk-main/**/highrise', recursive=True)
sdk_folder = os.path.dirname(sdk_paths[0])
sys.path.append(sdk_folder)

from highrise import BaseBot, Highrise

class Bot(BaseBot):
    async def on_start(self, session):
        print("Bot started! Connected to Highrise ✅")
        await self.highrise.chat("Bot en ligne! 👋")

    async def on_chat(self, user, message):
        print(f"{user.username}: {message}")
        if message.lower() == "salut":
            await self.highrise.chat(f"Salut {user.username} 👋")

async def main():
    token = os.getenv("HIGHRISE_TOKEN")
    room_id = os.getenv("ROOM_ID")

    if not token or not room_id:
        print("ERROR: HIGHRISE_TOKEN or ROOM_ID missing")
        exit(1)

    # CONNEXION WEBSOCKET POUR TON SDK
    uri = f"wss://api.highrise.game/websocket/{room_id}"
    async with websockets.connect(uri, extra_headers={"Authorization": f"Bearer {token}"}) as websocket:
        bot = Bot()
        bot.highrise = Highrise()
        await bot.on_start(None)

        while True:
            msg = await websocket.recv()
            data = json.loads(msg)
            print(data)

if __name__ == "__main__":
    asyncio.run(main())
