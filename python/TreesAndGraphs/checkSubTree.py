from tkinter.tix import Tree

from numpy import true_divide


def containsTree1(t1, t2):
    traversal1 = str(None)
    traversal2 = str(None)

    getPreOrderedTraversal(t1, traversal1)
    getPreOrderedTraversal(t2, traversal2)

    return traversal1.index(traversal2) != -1

def getPreOrderedTraversal(root, traversalList):
    if root == None:
        traversalList + "X"
        return
    traversalList + str(root.data)
    getPreOrderedTraversal(root.left, traversalList)
    
def containsTree(t1, t2):
    if t2 == None:
        return True
    return subTree(t1, t2)

def subTree(t1, t2):
    if t1 == None:
        return False
    if t1.data == t2.data and matchTree(t1, t2):
        return True 
    return subTree(t1.left, t2) or subTree(t2.right, t2)

def matchTree(r1, r2):
    if r1 == None and r2 == None:
        return True
    if r1 == None or r2 == None:
        return False
    if r1.data != r2.data:
        return False
    if r1.data == r2.data:
        return matchTree(r1.left, r2.left) and matchTree(r1.right, r2.right)

