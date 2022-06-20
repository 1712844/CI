from pickletools import stackslice
from queue import Empty
from numpy import empty
import stack

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
        if (self.stack is Empty):
            return True
    
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
            self.stacks.append(stack.Stack())
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
            removedItem = self.shift()
                
        
        