import time

async def progress(current, total, message, start):

    now = time.time()
    diff = now - start

    speed = current / diff if diff else 0
    percent = current * 100 / total

    filled = int(percent // 5)
    bar = "█" * filled + "░" * (20 - filled)

    text = f"""
╭━━━〔 ⚙️ Processing 〕━━━╮

📊 Progress:
[{bar}]

📈 {percent:.2f} %

⚡ Speed: {speed/1024/1024:.2f} MB/s
📦 Done: {current/1024/1024:.2f} MB
📁 Total: {total/1024/1024:.2f} MB

╰━━━━━━━━━━━━━━━━━━━━╯
"""

    try:
        await message.edit_text(text)
    except:
        pass
