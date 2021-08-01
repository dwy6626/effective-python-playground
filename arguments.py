def log(message, *values):
    print(type(values))
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')


log('My numbers are', 1, 2)
log('Hi there')


def func(a, b, op1=None):
    print(a, b, op1)

func(1, 2, 3)

my_options = {
    'op1': True,
}
func(1, 2, **my_options)
