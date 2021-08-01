from collections import namedtuple


Grade = namedtuple('Grade', ('score', 'weight'))

g = Grade(1, 3)
print(Grade)
print(g)
print(g.weight)
