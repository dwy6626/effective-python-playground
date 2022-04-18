from queue import Queue
from threading import Thread
queue = Queue(1)  # buffer size is 1

def consumer():
    print('consumer waiting')
    queue.get()
    print('consumer working')
    print('consumer done')
    queue.task_done()

thread = Thread(target=consumer)
thread.start()
print('producer putting')
queue.put(object())
queue.join()
print('producer done')
thread.join()
