class Node:
    def __init__(self):
        self.data = 0
        self.next = None

class LL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, val):
        newnode = Node()
        newnode.data = val

        if self.head is None and self.tail is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode

    def insert_at_front(self, val):
        newnode = Node()
        newnode.data = val

        if self.head is None and self.tail is None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def del_at_end(self):
        if self.head is None:  # Case 1: empty list
            print("As empty as humanly possible")
            return

        if self.head == self.tail:  # Case 2: single-node list
            self.head = None
            self.tail = None
            return

        # Case 3: multi-node list
        current = self.head
        while current.next.next is not None:  # stop at second-to-last
            current = current.next

        current.next = None
        self.tail = current

    def del_in_front(self):
        if self.head is None:  # Case 1: empty list
            print("As empty as humanly possible")
            return

        self.head = self.head.next

        if self.head is None:  # Case 2: list became empty
            self.tail = None

    def insert_at_idx(self,val, idx):
        newnode = Node()
        newnode.data = val

        count = 0
        current = self.head

        while count < idx:
            current = current.next
            count += 1

        print(current.data, ' heelo')

    def traverse(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

ll = LL()

ll.insert_at_end(5)
ll.insert_at_end(2)
ll.insert_at_end(7)
ll.insert_at_end(20)
ll.insert_at_end(12)
ll.insert_at_front(2)
ll.insert_at_front(78)
ll.insert_at_idx(99, 3)

#ll.traverse()