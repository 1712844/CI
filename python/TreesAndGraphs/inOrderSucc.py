from bt import Tree, STATE, Node

def inOrderSuccessor(node):
    if node is None:
        return None
    if node.right != None:
        return leftMostChild(node)
    else:


def leftMostChild(node):
    if node == None:
        return None
    while node.left != None:
        node = node.left
    return node