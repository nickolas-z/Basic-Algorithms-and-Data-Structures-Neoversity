# Через список
customers = []

def add_element(queue, el, priority):
    if len(queue) > 1:
           queue.append((priority, el))
           queue.sort(reverse=True)
    else:
        queue.append((priority, el))

add_element(customers, "a", 1)
add_element(customers, "b", 3)
add_element(customers, "c", 2)
add_element(customers, "d", 4)
add_element(customers, "e", 2)

while customers:
     print(customers.pop(0))



# Через heapq
import heapq

customers = []

heapq.heappush(customers, (2, "Harry"))
heapq.heappush(customers, (3, "Charles"))
heapq.heappush(customers, (1, "Riya"))
heapq.heappush(customers, (4, "Stacy"))

while customers:
     print(heapq.heappop(customers))



# Через PriorityQueue
from queue import PriorityQueue

customers = PriorityQueue()

customers.put((2, "Harry"))
customers.put((3, "Charles"))
customers.put((1, "Riya"))
customers.put((4, "Stacy"))

while not customers.empty():
     print(customers.get())


# Custom порівняння

import queue

class ComparableItem:
    def __init__(self, priority, item):
        self.priority = priority
        self.item = item

    def __lt__(self, other):
        # Change the comparison logic here to reverse the sorting order
        return self.priority < other.priority

# Example items
items = [(1, 'apple'), (3, 'banana'), (2, 'orange')]

# Wrap items with ComparableItem and enqueue them
pq = queue.PriorityQueue()
for priority, item in items:
    pq.put(ComparableItem(priority, item))

# Dequeue items
while not pq.empty():
    print(pq.get().item)
