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

    def partition(self, pivot):
        node = self.head
        head = self.head
        tail = self.head
        while (node is not None):
            next = node.next
            if (node.val < pivot):
                node.next = head
                head = node
            else:
                tail.next = node
                tail = node
            node = next
        tail.next = None
        return head

#2.2 (recursively)
def fromKthToLastRecursively(head, k, i):
    if head is None:
        return None, i
    node, i = fromKthToLastRecursively(head.next, k, i)
    i += 1
    # print(head.val)
    print("i = " + str(i))
    if (i == k):
        return head, i
    return node, i

def printList(head):
    if head is None:
        return None
    cur = head
    while (cur):
        print(" %d" %(cur.val))
        cur = cur.next
    return

#2.5 iterative 
def sumLists(head1, head2):
    p1 = head1
    p2 = head2
    result = LinkedList()
    runner = result
    carry = 0
    while (not (p1 is None and p2 is None)):
        val1 = p1.val if p1 is not None else 0
        val2 = p2.val if p2 is not None else 0
        value = val1 + val2 + carry
        if (result is None):
            result = Node(value % 10)
        result.next = Node(value % 10)
        if (value >= 10):
            carry = 1
        else:
            carry = 0
        p1 = p1.next if p1 is not None else p1
        p2 = p2.next if p2 is not None else p2
        if (p1 is None and p2 is None and carry == 1):
            print("value: " + str(value))
            result.next.next = Node(1)
        result = result.next
        print(result.val)
    return runner

#2.5 recursive
def sumLists(l1, l2, carry):
    if (l1 is None and l2 is None and carry == 0):
        return None
    result = Node(None)
    value = carry
    if (l1 is not None):
        value += l1.val
    if (l2 is not None):
        value += l2.val
    result.val = value % 10
    if (l1 is not None or l2 is not None):
        more = sumLists(
            l1.next if l1 is not None else None,
            l2.next if l2 is not None else None,
            1 if value >= 10 else 0
        )
        result.setNext(more)
    return result

def isPalindrome(self):
    slow = self.head
    fast = self.head  
    stack = []
    while (fast is not None and fast.next is not None):
        stack.insert(0, slow.val)
        slow = slow.next
        fast = fast.next.next
    if (fast is not None):
        slow = slow.next
    while(slow is not None):
        top = stack.pop(0)
        if (top != slow.val):
            return False
        slow = slow.next
    return True

def main():
    linkedList = LinkedList()
    linkedList.push(3)
    linkedList.push(5)
    linkedList.push(2) 
    linkedList.push(4)
    linkedList.push(3)
    linkedList.push(2)
    linkedList.push(1)
    ll, i = fromKthToLastRecursively(linkedList.head, 3, 0)
    printList(ll)

