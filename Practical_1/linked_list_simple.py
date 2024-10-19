class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

    def print_list(self):
        current = self
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Function to add a new node
def pushNode(head_ref, data_val):
    # Allocate node
    new_node = Node(data_val)
    # Link the old list of the new node
    new_node.next = head_ref[0]
    # Set the previous node of the current head to the new node
    if head_ref[0] is not None:
        head_ref[0].prev = new_node
    # Move the head to point to the new node
    head_ref[0] = new_node

# Function to get the middle of the linked list
def getMiddle(head):
    # Initialize the slow and fast pointer to the head of
    # the linked list
    slow_ptr = head
    fast_ptr = head

    while fast_ptr is not None and fast_ptr.next is not None:
        # Move the fast pointer by two nodes
        fast_ptr = fast_ptr.next.next
        # Move the slow pointer by one node
        slow_ptr = slow_ptr.next

    # If the total number of elements is even, move the slow pointer one step back
    if fast_ptr is None:
        slow_ptr = slow_ptr.prev

    return slow_ptr.data

# Driver Code
head = [None]
for i in range(6, 0, -1):
    pushNode(head, i)
    head[0].print_list()
    print("Middle Value Of Linked List is:", getMiddle(head[0]))