import asyncio

class HighriseBot:
    def __init__(self, session_metadata):
        self.session = session_metadata
    
    async def run(self):
        print(f"Bot démarré dans la room: {self.session.room_id}")
        while True:
            await asyncio.sleep(1)
