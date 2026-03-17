import asyncio
import os

async def aria2_download(url, output):

    cmd = [
        "aria2c",
        "-x", "16",   # 16 connections
        "-s", "16",   # 16 segments
        "-k", "1M",   # chunk size
        "-o", output,
        url
    ]

    process = await asyncio.create_subprocess_exec(*cmd)
    await process.wait()

    return output
