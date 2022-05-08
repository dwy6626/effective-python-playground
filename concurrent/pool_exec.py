import time, os
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

# def slow_io(n):
#     os.system(f'sleep {n}')

def slow_io(n):
    time.sleep(n)

N_JOB = 4
N_POOL = 4
NUMBERS = [1 for _ in range(N_JOB)]

def main():
    start = time.time()
    results = list(map(slow_io, NUMBERS))
    end = time.time()
    delta = end - start
    print(f'Took {delta:.3f} seconds')

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
    # main()
    main_thread()
    main_process()
