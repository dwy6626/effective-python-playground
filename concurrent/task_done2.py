from queue import Queue
from threading import Thread
queue = Queue(1)  # buffer size is 1
task_count = 3

def consumer():
    print('consumer waiting')
    for i in range(task_count):
        queue.get()
        print('consumer working', i + 1)
        print('consumer done', i + 1)
        queue.task_done()

thread = Thread(target=consumer)
thread.start()
print('producer putting')
for i in range(task_count):
    queue.put(object())
    print('producer put', i + 1)
queue.join()
print('producer done')
thread.join()
