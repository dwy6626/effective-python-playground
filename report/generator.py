def range(n):
    i = 0
    while i < n:
        yield i
        i += 1

for i in range(4):
    print(i)

for i in range(4):
    print(i)

print(range(3))
