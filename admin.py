from database.db import add_admin, ban, unban
from config import OWNER_ID

async def add_admin_cmd(client, message):

    if message.from_user.id != OWNER_ID:
        return

    uid = int(message.command[1])

    add_admin(uid)

    await message.reply_text("Admin Added😮‍💨.")
