import time, random
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

N_JOB = 100
N_POOL = 4
NUMBERS = [(random.randint(100000, 900000), random.randint(100000, 900000)) for _ in range(N_JOB)]

def main_thread():
    start = time.time()
    pool = ThreadPoolExecutor(max_workers=N_POOL)
    list(pool.map(gcd, NUMBERS))
    print(f'Took {time.time() - start:.3f} seconds')

def main_process():
    start = time.time()
    pool = ProcessPoolExecutor(max_workers=N_POOL)
    list(pool.map(gcd, NUMBERS))
    print(f'Took {time.time() - start:.3f} seconds')

if __name__ == '__main__':
    # main()
    main_thread()
    main_process()
