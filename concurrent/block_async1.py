import time
import asyncio

N_TASK = 10

async def slow_coroutine():
    time.sleep(0.1)

async def fan_out():
    coros = [slow_coroutine() for _ in range(N_TASK)]
    await asyncio.gather(*coros)

start = time.time()
# asyncio.run(fan_out())
asyncio.run(fan_out(), debug=True)
print(f'Took {time.time() - start:.3f} seconds')
