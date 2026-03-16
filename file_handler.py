import os
from config import DOWNLOAD_DIR

async def handle_file(client, message):

    file = await message.download(
        file_name=f"{DOWNLOAD_DIR}/"
    )

    await message.reply_text(
        "File received. Choose operation."
    )
