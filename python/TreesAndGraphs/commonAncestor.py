from bt import Tree, Node

#nodes with parents links
def commonAncestor(root, p, q):
    if not covers(root, q) or not covers(root, p):
        return root
    if covers(p, q):
        return p
    if covers(q, p):
        return q
    
    sibling = getSibling(p)
    parent = p.parent
    while(not covers(sibling, q)):
        parent = parent.parent
        sibling = getSibling(parent)
    return parent

def covers(root, p):
    if root is None:
        return False
    if p is None:
        return True
    return covers(root.left, p) or covers(root.right, p)

def getSibling(node):
    if node is None or node.parent is None:
        return None
    parent = node.parent
    return parent.left if parent.left is not None else parent.right