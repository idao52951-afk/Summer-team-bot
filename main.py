import os
print("TOKEN:", os.getenv("HIGHRISE_TOKEN"))
print("ROOM:", os.getenv("ROOM_ID"))
print("En attente 10s pour voir les logs...")
import time
time.sleep(10)
