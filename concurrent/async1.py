import asyncio

async def slow_io():
    await asyncio.sleep(1)

async def main():
    # create a coroutine
    coro = slow_io()
    # create_task will "run" the job ASAP
    task = asyncio.create_task(coro)
    # wait until "resolved"
    await task

# Python 3.7+
asyncio.run(main())
