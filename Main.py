import asyncio
import os
from highrise import HighriseBot, SessionMetadata

async def main():
    bot_token = os.getenv("HIGHRISE_TOKEN")
    room_id = os.getenv("ROOM_ID")
    
    if not bot_token or not room_id:
        print("ERROR: Mets HIGHRISE_TOKEN et ROOM_ID dans les Secrets de Render")
        return

    session_metadata = SessionMetadata(bot_token=bot_token, room_id=room_id)
    bot = HighriseBot(session_metadata)
    await bot.run()

if __name__ == "__main__":
    asyncio.run(main())
