import math
from unittest import result
from StackAndQueue.queue import Queue

import enum

class STATE(enum.Enum):
    UNVISITED = "UNVISITED"
    VISITED = "VISITED"
    VISITING = "VISITING"

class Node():
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        self.parent = None

class Tree():
    def __init__(self, head):
        self.head = head

    def add(self, node):
        if node is not None:
            self.append(node)


     
def createMinimalBST(arr, start, end):
    if end < start:
        return None
    mid = (start + end) / 2
    n = Node(arr[mid])
    n.left = createMinimalBST(arr, start, mid - 1)
    n.right = createMinimalBST(arr, mid + 1, end)
    return n
    
def insert(root, data):
    if root == None:
        return Node(data)
    if root.data == data:
        return root
    if data < root.data:
        left = insert(root.left, data)
        root.left = left
        left.parent = root
    if data > root.data:
        right = insert(root.left, data)
        root.right = right
        right.parent = root
    return root

#DFS
def listsOfDepths(root, lists, level):
    if root is None:
        return
    list = []
    if len(lists) > level:
        lists.append(list)
    else:
        list = lists.get(level)
    list.add(root)
    listsOfDepths(root.left, lists, level) 
    listsOfDepths(root.right, lists, level)

#BFS
def listsOfDepths(root):
    lists = []
    cur = []
    if root is not None:
        cur.append(root)
    while len(cur) > 0:
        lists.append(cur)
        parents = cur
        cur = []
        for parent in parents:
            if parent.left is not None:
                cur.append(parent.left)
            if parent.right is not None:
                cur.append(parent.right)
    return lists
    
    
def createListsOfDepths(root):
    lists = []
    listsOfDepths(root, lists, 0)
    return lists

def checkHeight(root):
    if root is None:
        return -1
    leftHeight = checkHeight(root.left)
    if leftHeight == -1:
        return -1
    rightHeight = checkHeight(root.right)
    if rightHeight == -1:
        return -1
    if abs(leftHeight - rightHeight) > 1:
        return -1
    else:
        return max(leftHeight, rightHeight) + 1

def isBalanced(root):
    return checkHeight(root) != -1

