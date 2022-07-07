def getSubset(set):
    allSubsets = []
    max = 1 << len(set)
    for i in range(max):
        subset = convertIntToSet(i, set)
        allSubsets.append(subset)
    return allSubsets

def convertIntToSet(x, set):
    index = 0
    subset = []
    k = x
    while(k > 0):
        if k & 1:
            subset.append(set[index])
        index += 1
        k >>= 1
    return subset