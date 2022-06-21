from pickletools import stackslice
from queue import Empty
import stack

class Stack():
    def __init__(self, size, capacity):
        self.top = None
        self.bottom = None
        self.size = size
        self.capacity = capacity

    def join(above, below):
        if above is not None:
            above.below = below
        if below is not None:
            below.above = above

    def pop(self):
        t = self.top
        self.top = self.top.below
        self.size -= 1
        return t.data

    def push(self, data):
        if (self.size >= self.capacity):
            return False
        self.size += 1
        newNode = stack.Node(data)
        if (self.size == 1):
            self.bottom = newNode
        self.join(newNode, self.top)
        self.top = newNode
        return True
    
    def removeBottom(self):
        bottom = self.bottom
        bottom = bottom.above
        if (bottom is not None):
            bottom.below = None
        self.size -= 1
        return bottom.data

    def isEmpty(self):
        return self.size == 0

class SetOfStacks():
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity
    
    def get(self, index):
        if (self.isEmpty or index < 0 or index > len(self.stacks)):
            return
        return self.stacks[index]

    def getLastStack(self):
        if (self.stack is Empty):
            return None
        return self.get(len(self.stacks) - 1)

    def isEmpty(self):
        return self.stacks is Empty
    
    def remove(self):
        last = self.getLastStack()
        last = None

    def push(self, data):
        last = self.getLastStack()
        if (last.head is None and data is not None):
            return
        if last.getLen() < self.capacity:
            last.push(data)            
        else:
            self.stacks.append(Stack())
            newLast = self.getLastStack()
            newLast.push(data)

    def popAt(self, index, removeTop):
        stacksLen = len(self.stacks)
        indexStack = self.get(index)
        if indexStack.head is not None:
            indexStack.pop()
            if indexStack.getLen() == 0:
                self.remove(len(self.stacks) - 1)
    
    def shift(self, index, removeTop):
        indexStack = self.get(index)
        removedItem = None
        if removeTop:
            removedItem = indexStack.pop()
        else:
            removedItem = indexStack.removeBottom()
        if (indexStack.isEmpty()):
            self.stacks.remove(index)
        else:
            if (self.stacks.size() > index + 1):
                value = self.shift(index + 1, False)
                stack.push(value)
        return removedItem
                
        
        