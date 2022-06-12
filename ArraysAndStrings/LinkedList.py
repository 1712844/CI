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
    
    #2.2 (iteratively)
    def fromKthToLastIteratively(self, k):
        p1 = self.head
        p2 = self.head
        for i in range(k):
            if (p1 is None):
                return None
            p1 = p1.next
        while (p1 is not None):
            p1 = p1.next
            p2 = p2.next
        self.head = p2

    #2.2 (recursively)
    def fromKthToLastRecursively(self, head, k, i):
        if (head is None):
            return
        self.head = fromKthToLastRecursively(head.next, k, i)
        i = i + 1
        if (i == k):
            return h
        

def printLinkedList(head):
    cur = head
    while(cur):
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
    linkedList.fromKthToLastIteratively(3)
    linkedList.printList()


if __name__ == "__main__":
    main()