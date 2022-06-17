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

def listLen(list):
    len = 0
    cur = list
    if cur is None:
        return len
    while (cur is not None):
        len+=1
        cur = cur.next
    return len

class Wrapper(object):
    def __init__(self, carry):
        self.sum = None
        self.carry = carry
    

def sumLists(l1, l2):
    if l1 is None and l2 is None:
        return None
    len1 = listLen(l1)
    len2 = listLen(l2)
    if len1 < len2:
        l1 = padList(l1, len2 - len1)
    else:
        l2 = padList(l2, len1 - len2)
    result = sumListsHelper(l1, l2)
    if (result.carry == 1):
        result = insertBefore(result, 1)
    return result

def sumListsHelper(l1, l2):
    if l1 is None and l2 is None:
        sum = Wrapper(None, 0)
        return sum
    sum = sumListsHelper(l1.next, l2.next)
    value = sum.carry + l1.val + l2.val
    result = insertBefore(sum.sum, value)
    sum = result
    carry = value / 10
    return Wrapper(result, carry)

def insertBefore(list, value):
    new_node = Node(value)
    if (list is not None):
        new_node.next = list;
    return new_node

def padList(head, pad):
    if head is None or pad <= 0:
        return head
    for x in range(pad):
        head = insertBefore(head, 0)
    return head