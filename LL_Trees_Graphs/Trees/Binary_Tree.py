Q = []

class Node:
    def __init__(self):
        self.data = 0
        self.lc = None
        self.rc = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def createBinaryTree(self, val):
        new_node = Node()

        new_node.data = val

        if self.root is None:
            self.root = new_node
            return

        Q.append(self.root)

        while len(Q) > 0:
            p = Q.pop(0)
            
            if p.lc is None:
                p.lc = new_node
                return
            else:
                Q.append(p.lc)

            if p.rc is None:
                p.rc = new_node
                return
            else:
                Q.append(p.rc)

    def pre_order(self, p):
        if p is None:
            return

        print(p.data)
        self.pre_order(p.lc)
        self.pre_order(p.rc)

    def post_order(self, p):
        if p is None:
            return

        self.post_order(p.lc)
        self.post_order(p.rc)
        print(p.data)

    def in_order(self, p):
        if p is None:
            return

        self.in_order(p.lc)
        print(p.data)
        self.in_order(p.rc)

bt = BinaryTree()

bt.createBinaryTree(4)
bt.createBinaryTree(2)
bt.createBinaryTree(5)

bt.in_order(bt.root)