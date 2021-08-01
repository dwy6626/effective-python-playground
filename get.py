key = 'c'

some_dict = {
    'a': 2,
    'b': 1
}

# 兩次存取
if key in some_dict:
    value = some_dict[key]
else:
    value = 0

# 一次存取
try:
    value = some_dict[key]
except KeyError:
    value = 0

# 一次存取
value = some_dict.get(key, 0)
value = some_dict.get(key)

value = some_dict.setdefault(key, 1)
print(value)

