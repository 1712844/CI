from lib2to3.pytree import Node
import random

class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.size = 0

    def getRandomNode(self):
        leftSize = self.left if self.left != None else 0
        rand = random.randint(0, leftSize)
        if (rand < leftSize):
            return self.left.getRandomNode()
        if rand == leftSize:
            return self
        else:
            return self.right.getRandomNode()

    def insertInOrder(self, d):
        if d <= self.data:
            if self.left != None:
                self.left = TreeNode(d)
            else:
                self.left = self.insertInOrder(self.left, d)
        else:
            if self.right != None:
                self.right = TreeNode(d)
            else:
                self.right = self.insertInOrder(self.right, d)
        self.size+=1

    def getIthNode(self, i):
        leftSize = self.left if self.left != None else 0
        rand = random.randint(0, leftSize)
        if (rand < leftSize):
            return self.left.getIthNode(i)
        if rand == leftSize:
            return self
        else:
            return self.right.getRandomNode(i - (leftSize + 1))

class Tree():
    def __init__(self):
        self.root = TreeNode(None)
        self.size = self.root.size 
    
    def insertOrder(self, data):
        if self.root == None:
            return TreeNode(data)
        else:
            self.root.insertInOrder(data)

    def getRandomNode(self):
        if self.root == None:
            return None
        return self.getIthNode(random.randint(self.size))
    