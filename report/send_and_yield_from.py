def step_mul(steps):
    amplitude = yield
    for step in range(steps):
        amplitude = yield amplitude * step


def complex_step_mul():
    yield from step_mul(3)
    yield from step_mul(4)

def run_modulating(it):
    amplitudes = [
        None, 7, 7, 7, 2, 2, 2, 2]
    for amplitude in amplitudes:
        output = it.send(amplitude)
        print(f'Output: {output}')

run_modulating(complex_step_mul())
