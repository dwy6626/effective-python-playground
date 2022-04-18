from queue import Queue
from threading import Thread
queue = Queue(1)  # buffer size is 1

def consumer():
    print('consumer waiting')
    queue.get()  # block, wait until some data are put
    print('consumer get 1')
    queue.get()
    print('consumer get 2')

thread = Thread(target=consumer)
thread.start()

print('producer putting')
queue.put(object())
print('producer put 1')
queue.put(object())
print('producer put 2')
thread.join()
