class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Queue():
    def __init__(self):
        self.first = None
        self.last = None

    def isEmpty(self):
        return self.first == None
        

    def add(self, data):
        newNode = Node(data)
        if (self.first is not None):
            self.last.next = newNode
        self.last = newNode
        if (self.first is None):
            self.first = self.last

    def remove(self):
        if self.first is None:
            return None
        result = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = self.first
        return result
        
    def peek(self):
        if self.first is None:
            return None
        return self.first.data

    # def getLen(self):
    #     if self.head is None:
    #         return None
    #     cur = self.head
    #     count = 0
    #     while(cur):
    #         count+=1
    #         cur = cur.next
    #     return count

    # def printStack(self):
    #     if self.head is None:
    #         print("Stack is empty")
    #     cur = self.head
    #     while(cur):
    #         print(cur.data)
    #         cur = cur.next
    #     return