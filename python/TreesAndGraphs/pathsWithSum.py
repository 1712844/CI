from bt import Node

def pathWithSumFromGivenNode(node, target, currentSum):
    if node == None:
        return None
    currentSum += node.data
    totalPaths = 0
    if currentSum == target:
        totalPaths+=1
    totalPaths += pathWithSumFromGivenNode(node.left, target, currentSum)
    totalPaths += pathWithSumFromGivenNode(node.right, target, currentSum)
    return totalPaths

def pathWithSum(root, target):
    if root == None:
        return None
    return pathWithSumFromGivenNode(root, target) + pathWithSumFromGivenNode(root.left, tar)