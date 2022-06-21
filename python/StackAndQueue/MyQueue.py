from stack import Stack, Node

def MyQueue():
    def __init__(self):
        self.newStack = Stack()
        self.oldStack = Stack()

    def add(self, data):
        self.newStack.push(Node(data))

    def shift(self):
        if (self.oldStack.isEmpty()):
            while(not self.newStack.isEmpty()):
                self.oldStack.push(self.newStack.pop())

    def peek(self):
        self.shift()
        return self.oldStack.head.data
    
    def remove(self):
        self.shift()
        return self.oldStack.pop()