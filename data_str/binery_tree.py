from symbol import yield_arg


class binery_tree:

    def __init__(self, rootObj):
        self.key = rootObj
        self.rightChild = None
        self.leftChild = None


    def insertRight(self, right):
        if self.rightChild == None:
            self.rightChild = binery_tree(right)
        else:
            t = binery_tree(right)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertLeft(self, left):
        if 

