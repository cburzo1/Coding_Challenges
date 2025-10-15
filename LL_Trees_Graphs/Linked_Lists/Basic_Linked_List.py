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

            newnode.next = current.next
            current.next = newnode

        self.length += 1

    def create_cycle(self, head, tail, idx):
        current = head
        count = 0

        while count < 1:
            current = current.next
            count += 1

        tail.next = current

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

            to_delete = current.next
            current.next = current.next.next
            to_delete = None

        self.length -= 1

class LL_OPs:

    def reverse(self, head, tail):
        oldhead = head
        head = tail
        tail = oldhead
        oldhead = None

        p = tail.next
        t = p.next
        r = tail
        tail.next = None

        while t.next is not None:
            p.next = r
            r = p
            p = t
            t = t.next

        p.next = r
        t.next = p

        return head

    def sort_list(self, head, siz):
        p = head
        t = head.next
        i = siz
        while i > 0:
            while t is not None:
                if p.data > t.data:
                    temp = p.data
                    p.data = t.data
                    t.data = temp

                p = p.next
                t = t.next

            p = head
            t = head.next
            i -= 1

        return head

    def merged_sorted_lists(self, head_1, head_2):
        ll_3 = LL()
        p = head_1
        t = head_2

        while p is not None and t.next is not None:
            print(p.data, t.data)
            if p.data < t.data:
                ll_3.insert_at_end(p.data)
                p = p.next
            else:
                ll_3.insert_at_end(t.data)
                t = t.next

        while p is not None:
            ll_3.insert_at_end(p.data)
            p = p.next

        while t is not None:
            ll_3.insert_at_end(t.data)
            t = t.next

        self.traverse(ll_3.head)

    def traverse(self, head):
        current = head

        while current is not None:
            print(current.data, end = " ")
            current = current.next

    def detect_cycle(self, head):
        p = head
        t = head

        while t is not None and t.next is not None:
            p = p.next
            t = t.next.next

            if p is t:
                return True  # cycle detected

        return False  # reached end → no cycle

ll_1 = LL()
ll_ops = LL_OPs()

ll_1.insert_at_end(5)
ll_1.insert_at_end(2)
ll_1.insert_at_end(7)
ll_1.insert_at_end(4)

ll_1.create_cycle(ll_1.head, ll_1.tail, 1)

print(ll_ops.detect_cycle(ll_1.head))

'''ll_ops.traverse(ll_1_sorted)
print()
ll_ops.traverse(ll_2_sorted)'''