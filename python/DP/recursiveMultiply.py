def recursiveMultiple(a, b):
    if a == 0 | b == 0:
        return 0
    return recursiveMultiply(a, b)

def recursiveMultiply(a, b):
    if b == 0:
        return 0
    a += recursiveMultiply(a, b - 1)
    return a

def minProduct2(a, b):
    bigger = a if a > b else b
    smaller = a if a < b else b
    return minProductHelper(smaller, bigger)

def minProductHelper(smaller, bigger):
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger
    
    s = smaller >> 1
    halfProd = minProductHelper(s, bigger)

    if (smaller % 2 == 0):
        return halfProd + halfProd
    else:
        return halfProd + halfProd +bigger

def minProduct(a, b):
    bigger = a if a > b else b
    smaller = a if a < b else b
    memo = [None] * (smaller + 1)
    return minProductHelp(smaller, bigger, memo)

def minProductHelp(smaller, bigger, memo):
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger
    if memo[smaller] != None:
        return memo[smaller]
    
    s = smaller >> 1
    side1 = minProduct(s, bigger, memo)
    side2 = side1
    
    if side1 % 2 == 1:
        side1 = minProduct(smaller - s, bigger memo)
    memo[smaller] = side1 + side2
    return memo[smaller]