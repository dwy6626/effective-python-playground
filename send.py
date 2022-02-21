def my_generator():
    received = yield 1
    print(f'received: {received}')

it = my_generator()
output = it.send(None)  # generator 剛開始，還沒有碰到 yield 時，只能接收 None
print(f'output: {output}')

try:
    while (output := it.send('hello')):
        print('will not come here')
except StopIteration:
    pass
