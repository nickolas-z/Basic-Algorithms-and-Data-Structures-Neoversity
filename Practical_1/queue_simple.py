import time
 
# Через список
start = time.time()

queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print("Initial queue", queue)
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
queue.append('d')
print(queue.pop(0))
print(queue.pop(0))

print(time.time() - start)
print("\nQueue after removing elements", queue)





from collections import deque

# Через deque
start = time.time()
q = deque()
q.append('a')
q.append('b')
q.append('c')
print("Initial queue", q)
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
q.append('d')
print(q.popleft())
print(q.popleft())
 
print(time.time() - start)
print("\nQueue after removing elements", q)




from queue import Queue

start = time.time()
q = Queue(maxsize = 4)

q.put('a')
q.put('b')
q.put('c')
print("Initial queue", q.queue)
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
q.put('d')
print(q.get())
print(q.get())
print(time.time() - start)

print("\nQueue after removing elements", q.queue)

