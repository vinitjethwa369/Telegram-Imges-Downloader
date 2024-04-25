import os
import asyncio
from datetime import datetime
from telethon.sync import TelegramClient

# Replace these values with your own
api_id = ''
api_hash = ''
phone_number = ''

# Function to download media files and organize them into folders based on file extensions
async def download_media(api_id, api_hash, phone_number, group_name):
    client = TelegramClient(phone_number, api_id, api_hash)
    await client.start()

    # Create a directory to save media files
    os.makedirs(group_name, exist_ok=True)

    # Iterate over messages in the group
    async for message in client.iter_messages(group_name):
        if message.media:
            # Get the date of the media message
            date = message.date.strftime('%Y-%m-%d')

            # Get the file extension
            file_ext = ''
            if message.photo:
                file_ext = 'jpg'
            elif message.video:
                file_ext = 'mp4'
            elif message.audio:
                file_ext = 'mp3'
            elif message.document:
                file_ext = message.document.mime_type.split('/')[-1]  # Get file extension from MIME type
            else:
                # Skip unsupported media types
                continue

            # Download the media file
            file_name = f"{date}.{file_ext}"
            await client.download_media(message.media, file=os.path.join(group_name, file_ext, file_name))

    await client.disconnect()

# Entry point
async def main():
    await download_media(api_id, api_hash, phone_number, "iHariPrabodham")

# Run the main coroutine
asyncio.run(main())