import itertools, functools

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# accumulate
print(list(itertools.accumulate(values)))
# [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
print(list(itertools.accumulate(values, lambda x, y: (x + y) % 20)))
# [1, 3, 6, 10, 15, 1, 8, 16, 5, 15]

# reduce 只會回傳最後結果，而 accumulate 會每步回傳
print(functools.reduce(lambda x, y: x + y, values))
# 55

# product: Cartesian product of 2 iterators
it1 = 'abc'
it2 = [1, 2]
print(list(itertools.product(it1, it2)))
# [('a', 1), ('a', 2), ('b', 1), ('b', 2), ('c', 1), ('c', 2)]
print(list(itertools.product(it2, repeat=3)))  # 和自己 prodcut
# [(1, 1, 1), (1, 1, 2), (1, 2, 1), (1, 2, 2), (2, 1, 1), (2, 1, 2), (2, 2, 1), (2, 2, 2)]

# 高中排列組合三大天王
print(list(itertools.permutations(it1, 2)))
# [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
print(list(itertools.combinations(it1, 2)))
# [('a', 'b'), ('a', 'c'), ('b', 'c')]
print(list(itertools.combinations_with_replacement(it1, 2)))
# [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]
