class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def deleteNode(self, val):
        cur = self.head
        
        if (cur is not None and cur.val == val):
            self.head = cur.next
            cur = None
            return
        
        while (cur.next is not None):
            if cur.next.val == val:
                cur.next = cur.next.next
                return
            cur = cur.next
        return
    
    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
    
    def printList(self):
        cur = self.head
        while(cur):
            print(" %d" %(cur.val))
            cur = cur.next
        return
    
    def getNode(self, pos):
        cur = self.head
        while (pos > 0 and cur.next is not None):
            pos = pos - 1
            cur = cur.next
            print(cur.val)
        return cur
            
    #2.1
    def removeDups(self):
        if self.head is None or self.head.next is None:
            return
        
        cur = self.head
        table = [cur.val] 
        while (cur.next is not None):
            if (cur.next.val in table):
                cur.next = cur.next.next
            else:
                table.append(cur.next.val)
                cur = cur.next
        return

    def removeMiddleNode(node):
        if (node is not None and node.next is not None):
            return
        node.val = node.next.val
        node.next = node.next.next
        return 

def printList(head):
    if head is None:
        return None
    cur = head
    while (cur):
        print(" %d" %(cur.val))
        cur = cur.next
    return

def main():
    linkedList = LinkedList()
    linkedList.push(3)
    linkedList.push(5)
    linkedList.push(2) 
    linkedList.push(4)
    linkedList.push(3)
    linkedList.push(2)
    linkedList.push(1)
    node = linkedList.getNode(3)    
    print(node.val)

if __name__ == "__main__":
    main()