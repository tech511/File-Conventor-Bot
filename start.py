from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.db import start_image
from config import OWNER_USERNAME, UPDATE_CHANNEL

async def start(client, message):

    text = f"""
Hi {message.from_user.first_name}

_I Am Advance Zip File Maker And Extractor Bot.
I Can Convert Any Video Or Files Into Zip Files._

Maintain By:- @{AniWorld_Bot_Hub}
"""

    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Owner", url=f"https://t.me/{OWNER_USERNAME}")],
            [InlineKeyboardButton("Update Channel", url=UPDATE_CHANNEL)]
        ]
    )

    if start_image:

        await message.reply_photo(
            start_image,
            caption=text,
            reply_markup=buttons
        )

    else:

        await message.reply_text(text, reply_markup=buttons)
