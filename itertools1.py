import itertools

it1 = [1, 2, 3, 4]
it2 = [5, 6, 7, 8]

# chain: 結合 iterators
print(list(itertools.chain(it1, it2)))
# [1, 2, 3, 4, 5, 6, 7, 8]

# repeat: 重複一個值 
print(list(itertools.repeat('hello', 3)))
# ['hello', 'hello', 'hello'

# cycle: 不斷重複一個 iterator
it = itertools.cycle(it1)
print([next(it) for _ in range(9)])
# [1, 2, 3, 4, 1, 2, 3, 4, 1]

# tee: 使用一個 iterator 產生平行的 iterators
it3, it4, it5 = itertools.tee(it1, 3)
print(list(it3))  # [1, 2, 3, 4]
print(list(it4))  # [1, 2, 3, 4]
print(list(it5))  # [1, 2, 3, 4]

# zip_longest:
it3 = [5, 6, 7]
print(list(zip(it1, it3)))
# [(1, 5), (2, 6), (3, 7)]
print(list(itertools.zip_longest(it1, it3, fillvalue='NA')))
# [(1, 5), (2, 6), (3, 7), (4, 'NA')]
