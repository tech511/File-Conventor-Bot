import asyncio
from pyrogram import Client, filters

from config import BOT_TOKEN, API_ID, API_HASH
from handlers.start import start
from handlers.batch import batch
from handlers.file_handler import handle_file
from handlers.admin import add_admin_cmd

app = Client(
    "zipbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=8
)

app.add_handler(filters.command("start")(start))
app.add_handler(filters.command("batch")(batch))
app.add_handler(filters.command("add_admin")(add_admin_cmd))

app.add_handler(filters.document | filters.video | filters.audio)(handle_file)

async def main():

    await app.start()

    print("Bot Running...")

    await idle()

if __name__ == "__main__":
    asyncio.run(main())
