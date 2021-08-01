import itertools

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# islice: 當作 list 做 slicing
# end (inclusive! 和 list 行為不同)
print(list(itertools.islice(values, 5)))       # [1, 2, 3, 4, 5]
# start + end
print(list(itertools.islice(values, 2, 4)))    # [3, 4]
# start + end + step
print(list(itertools.islice(values, 1, 7, 2))) # [2, 4, 6]

# takewhile, dropwhile
print(list(itertools.takewhile(lambda x: x < 4, values)))
# [1, 2, 3]
print(list(itertools.dropwhile(lambda x: x > 4, values)))
# [1, 2, 3]

# filterfalse: 反向 filter / reject
print(list(filter(lambda x: x % 3 == 0, values)))
# [3, 6, 9]
print(list(itertools.filterfalse(lambda x: x % 3 == 0, values)))
# [1, 2, 4, 5, 7, 8, 10]
