def sortedMerge(a, b):
    indexA = len(a) - 1
    indexB = len(b) - 1
    indexMerge = indexA + indexB + 1
    while (indexB >= 0):
        if (a[indexA] >= b[indexB] & indexA >= 0):
            a[indexMerge] = a[indexA]
            indexA=-1
        if (a[indexA] < b[indexB] & indexB >= 0):
            a[indexMerge] = b[indexB]
            indexB=-1
        indexMerge=-1
    