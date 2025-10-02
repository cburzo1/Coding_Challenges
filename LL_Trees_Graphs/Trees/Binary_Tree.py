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

    def get_max_depth(self, p):
        if p is None:
                return -1

        # compute the height of left and right subtrees
        lHeight = self.get_max_depth(p.lc)
        rHeight = self.get_max_depth(p.rc)

        return max(lHeight, rHeight) + 1

    def level_order(self, p):

        Q = []

        if p is not None:
            print(p.data)
            Q.append(p)

        while len(Q) > 0:
            dq = Q.pop(0)

            if dq.lc is not None:
                print(dq.lc.data)
                Q.append(dq.lc)

            if dq.rc is not None:
                print(dq.rc.data)
                Q.append(dq.rc)

bt = BinaryTree()

bt.createBinaryTree('a')
bt.createBinaryTree('b')
bt.createBinaryTree('c')
bt.createBinaryTree('d')
bt.createBinaryTree('e')
bt.createBinaryTree(None)
bt.createBinaryTree(None)
bt.createBinaryTree(None)
bt.createBinaryTree(None)
bt.createBinaryTree('f')
bt.createBinaryTree(None)

bt.pre_order(bt.root)
print(bt.get_max_depth(bt.root))