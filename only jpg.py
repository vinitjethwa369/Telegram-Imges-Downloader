import os
import asyncio
from datetime import datetime
from telethon.sync import TelegramClient

# Replace these values with your own
api_id = ''
api_hash = ''
phone_number = ''

# Function to download images and organize them into folders based on date
async def download_images(api_id, api_hash, phone_number, group_name):
    client = TelegramClient(phone_number, api_id, api_hash)
    await client.start()

    # Create a directory to save images
    os.makedirs(group_name, exist_ok=True)

    # Iterate over messages in the group
    async for message in client.iter_messages(group_name):
        if message.photo:
            # Get the date of the photo
            date = message.date.strftime('%Y-%m-%d')
            # Download the photo
            await client.download_media(message.photo, file=os.path.join(group_name, date))

    await client.disconnect()

# Entry point
async def main():
    await download_images(api_id, api_hash, phone_number, "iHariPrabodham")

# Run the main coroutine
asyncio.run(main())
