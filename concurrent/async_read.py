import time, os
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

FILE = 'async_read.py'

def slow_io(n):
    for _ in range(n):
        with open(FILE, 'r') as f:
            f.readlines()

N_JOB = 2
N_POOL = 2
NUMBERS = [100 for _ in range(N_JOB)]

def main():
    start = time.time()
    list(map(slow_io, NUMBERS))
    print(f'Took {time.time() - start:.3f} seconds')

def main_thread():
    start = time.time()
    pool = ThreadPoolExecutor(max_workers=N_POOL)
    list(pool.map(slow_io, NUMBERS))
    print(f'Took {time.time() - start:.3f} seconds')

def main_process():
    start = time.time()
    pool = ProcessPoolExecutor(max_workers=N_POOL)
    list(pool.map(slow_io, NUMBERS))
    print(f'Took {time.time() - start:.3f} seconds')

if __name__ == '__main__':
    main()
    main_thread()
    main_process()
