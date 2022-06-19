from email import header
from logging.config import valid_ident
from operator import truediv
from tarfile import _Bz2ReadableFileobj
from urllib.parse import non_hierarchical


class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def setNext(self, next):
        self.next = next
    
    def getNext(self):
        return self.next
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
    
    def insertEnd(self, val):
        if self.head is None:
            self.haed
        

    def printList(self):
        cur = self.head
        while(cur):
            print(" %d" %(cur.val))
            cur = cur.next
    
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

    def reverseList(self):
        cur = self.head
        prev = None
        while (cur is not None):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

def findLoopBeginning(list):
    if list.head is None:
        return None
    slower = list.head
    faster = list.head
    while (faster is not None and faster.next is not None):
        faster = faster.next
        slower = slower.next
        if (slower == faster):
            break
    #None loop check
    if (faster is None or faster.next is None):
        return None

    slower = list.head
    while(faster != slower):
        faster = faster.next
        slower = slower.next

    return faster

def listLen(list):
    len = 0
    cur = list
    if cur is None:
        return len
    while (cur is not None):
        len+=1
        cur = cur.next
    return len

def printList(head):
    if head is None:
        return None
    cur = head
    print(cur.val)
    while (cur):
        print(" %d" %(cur.val))
        cur = cur.next
    return

def main():
    linkedList = LinkedList()
    linkedList.push(6)
    linkedList.push(1)
    linkedList.push(7)
    linkedList2 = LinkedList()
    linkedList2.push("a")
    linkedList2.push("b")
    linkedList2.push("c")
    linkedList2.push("b")
    linkedList2.push("a")
    # result = sumLists(linkedList.head, linkedList2.head, 0)
    result = linkedList2.isPalindrome()
    print(result)

if __name__ == "__main__":
    main()