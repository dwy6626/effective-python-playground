import random


class Timer:
    def __init__(self, period):
        self.current = period  # state
        self.period = period   # initial

    def reset(self):
        self.current = self.period

    def __iter__(self):
        while self.current:
            self.current -= 1
            yield self.current


def check_reset():
    return random.randint(0, 3) == 0

def run():
    timer = Timer(4)
    for current in timer:
        if check_reset():
            timer.reset()
        print(current)


run()
# 3
# 2
# 1
# 3
# 2
# 3
# 2
# 1
# 0