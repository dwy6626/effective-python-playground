def step_mul(amplitude_it, steps):
    for step in range(steps):
        amplitude = next(amplitude_it)
        yield amplitude * step

def complex_step_mul(amplitude_it):
    yield from step_mul(amplitude_it, 3)
    yield from step_mul(amplitude_it, 4)

def run_cascading():
    amplitudes = [7, 7, 7, 2, 2, 2, 2]
    it = complex_step_mul(iter(amplitudes))
    for _ in amplitudes:
        output = next(it)
        print(f'Output: {output}')

run_cascading()
