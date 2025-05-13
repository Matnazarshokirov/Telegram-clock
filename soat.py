from telethon.sync import TelegramClient
from datetime import datetime
import time

api_id = 4157011  # misol: 1234567
api_hash = 'c384255735fd7f1ef05d2f46ce6b329c'

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    while True:
        current_time = datetime.now().strftime("%H:%M")
        await client(UpdateProfileRequest(
            first_name=f"Matnazar | {current_time}"
        ))
        time.sleep(60)

with client:
    client.loop.run_until_complete(main())