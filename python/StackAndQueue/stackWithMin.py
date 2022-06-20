from urllib.parse import _NetlocResultMixinStr
from python.StackAndQueue.stack import Stack
import stack

class StackWithMin():
    def __init__(self):
        self.minStack = Stack()
        self.stack = Stack()

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def peek(self):
        if self.head is None:
            return None
        return self.head

    def min(self):
        return self.minStack.head if self.minStack.head else None

    def push(self, data):
        if (data < min.data):
            self.minStack.push(data)
        self.stack.push(data)
        
            
    