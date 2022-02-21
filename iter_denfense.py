import collections


def normalize_defensive(numbers):
    if iter(numbers) is numbers:  # iterator 的 __iter__ 會傳回自己
        raise TypeError('Must apply a container')
    total = sum(numbers)
    for value in numbers:
        percent = 100 * value / total
        yield percent

from collections.abc import Iterator

def normalize_defensive2(numbers):
    if isinstance(numbers, Iterator):
        raise TypeError('Must apply a container')
    total = sum(numbers)
    for value in numbers:
        percent = 100 * value / total
        yield percent

print(list(normalize_defensive2(range(23))))
