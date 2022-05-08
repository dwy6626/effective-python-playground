import time
import asyncio

N_TASK = 10

async def slow_io():
    await asyncio.sleep(0.1)

async def fan_out():
    coros = [slow_io() for _ in range(N_TASK)]
    await asyncio.gather(*coros)

start = time.time()
asyncio.run(fan_out())
print(f'Took {time.time() - start:.3f} seconds')
