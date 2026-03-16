import time

async def progress(current, total, message, start):

    now = time.time()
    diff = now - start

    speed = current / diff if diff > 0 else 0
    percent = current * 100 / total

    bar = "█" * int(percent/5) + "░" * (20-int(percent/5))

    text = f"""
📦 Processing File

[{bar}]

{percent:.2f} %

⚡ Speed: {speed/1024/1024:.2f} MB/s
"""

    await message.edit_text(text)
