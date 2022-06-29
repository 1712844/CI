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

#without parents linkg
def commonAncestor2(root, p, q):
    if not covers(root, p) or not covers(root, q):
        return None
    return ancestorHelper(root, p, q)

def ancestorHelper(root, p, q):
    if root is None or p is None or q is None:
        return None
    pOnLeft = covers(root.left, p)
    qOnLeft = covers(root.left, q)
    if (pOnLeft != qOnLeft){
        return root
    }
    childSide = root.left if pOnLeft else root.right
    return ancestorHelper(childSide, p, q)

def commonAncestor3(root, p, q):
    if root == None:
        return None
    if root == p or root == q:
        return root
    left = commonAncestor3(root.left, p, q)
    if (left != None and p != None and q != None):
        return left
    right = commonAncestor3(root.right, p, q)
    if (right != None and p != None and q != None):
        return right
    if (left != None and right != None):
        return root
    if (root == p or root == q):
        return root
    return right if left == None else left