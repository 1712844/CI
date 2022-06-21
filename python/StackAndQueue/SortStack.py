from re import L
from stack import Stack, Node

class SortStack():
    def __init__(self):
        self.dataStack = Stack()

    def sortStack(self):
        tempStack = Stack()
        while(not self.dataStack.isEmpty()):
            tmp = self.dataStack.pop()
            while (not tempStack.isEmpty() and tempStack.peek() > tmp.data):
                self.dataStack.push(tempStack.pop())
            tempStack.push(tmp)
        while(not tempStack.isEmpty()):
            self.dataStack.push(tempStack.pop())

            
            