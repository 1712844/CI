class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, data):
        if self.head is None:
            return None
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        if self.head is None:
            return None
        else:
            result = self.head
            self.head = self.head.next
            result.next = None
            return result

    def peek(self):
        if self.head is None:
            return None
        return self.head.data

    def getLen(self):
        if self.head is None:
            return None
        cur = self.head
        count = 0
        while(cur):
            count+=1
            cur = cur.next
        return count

    def printStack(self):
        if self.head is None:
            print("Stack is empty")
        cur = self.head
        while(cur):
            print(cur.data)
            cur = cur.next
        return

        
    