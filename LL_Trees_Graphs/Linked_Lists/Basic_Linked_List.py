class Node:
    def __init__(self):
        self.data = 0
        self.next = None

class LL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_at_end(self, val):
        newnode = Node()
        newnode.data = val

        if self.head is None and self.tail is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode

        self.length += 1

    def insert_at_front(self, val):
        newnode = Node()
        newnode.data = val

        if self.head is None and self.tail is None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head = newnode

        self.length += 1

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

        self.length -= 1

    def del_in_front(self):
        if self.head is None:  # Case 1: empty list
            print("As empty as humanly possible")
            return

        self.head = self.head.next

        if self.head is None:  # Case 2: list became empty
            self.tail = None

        self.length -= 1

    def insert_at_idx(self,val, idx):
        newnode = Node()
        newnode.data = val

        if idx >= self.length:
            self.insert_at_end(val)
        elif idx <= 0:
            self.insert_at_front(val)
        else:
            count = 0
            current = self.head

            while count < (idx - 1):
                current = current.next
                count += 1

            print(current.data, ' heelo')
            newnode.next = current.next
            current.next = newnode

        self.length += 1

    def delete_at_idx(self, idx):

        if self.head is None:
            print("LL is empty")
            return

        if idx >= self.length:
            self.del_at_end()
        elif idx <= 0:
            self.del_in_front()
        else:

            count = 0
            current = self.head

            while count < (idx - 1):
                current = current.next
                count += 1

            print(current.data, ' heelo')
            to_delete = current.next
            current.next = current.next.next
            to_delete = None

        self.length -= 1

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

ll.insert_at_idx(50, 2)
ll.delete_at_idx(3)
ll.delete_at_idx(3)
ll.delete_at_idx(3)
ll.delete_at_idx(2)
ll.delete_at_idx(2)
ll.delete_at_idx(1)
ll.delete_at_idx(0)
print()
ll.traverse()