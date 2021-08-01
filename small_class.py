from collections import defaultdict

current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
]

class CountMissing:
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0

counter = CountMissing()
print(callable(counter))    # True
result = defaultdict(counter, current)

for key, amount in increments:
    result[key] += amount

print(counter.added)         # 2
