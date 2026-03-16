user_batch = {}

async def batch(client, message):

    user = message.from_user.id

    user_batch[user] = []

    await message.reply_text(
        "Hlo Cutie🥰 Send Me Your Videos One By One😗."
    )
