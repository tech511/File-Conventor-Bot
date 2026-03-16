import asyncio

task_queue = asyncio.Queue()

async def add_task(task):
    await task_queue.put(task)

async def worker():

    while True:

        task = await task_queue.get()

        try:
            await task()
        except Exception as e:
            print("Task Error:", e)

        task_queue.task_done()
