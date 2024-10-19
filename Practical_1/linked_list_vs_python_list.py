import random
import time

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnOrderedList(object):
    def __init__(self):
        self.N = 0
        self.head = None

    def size(self):
        return self.N

    def is_empty(self):
        return self.N == 0

    def add(self, data):
        self.N += 1
        temp = Node(data)
        temp.set_next(self.head)
        self.head = temp

    def search(self, data):
        current = self.head
        found = False
        while current and not found:
            if current.get_data() == data:
                found = True
            current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        while current.get_data() != item:
            previous = current
            current = current.get_next()
        if not previous:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        self.N -= 1
        
        
for i in range(1000, 10000001, 1000000):
    list1 = []
    list2 = UnOrderedList()
    for a in range(i):
        list2.add(a)
        list1.append(a)

    a = random.randrange(0, i)

    start_time1 = time.time()
    list1.remove(a)
    end_time1 = time.time()

    start_time2 = time.time()
    list2.remove(a)
    end_time2 = time.time()

    print("List time remove: {0}. Linked List time remove: {1}".format(end_time1-start_time1, end_time2-start_time2))
    

list1 = []
list2 = UnOrderedList()
for i in range(1, 100):
        start_time1 = time.time()
        list2.add(i)
        end_time1 = time.time()
        
        start_time2 = time.time()
        list1.append(i)
        end_time2 = time.time()
        print("List time append: {0}. Linked List time add: {1}".format(end_time1-start_time1, end_time2-start_time2))