def magicIndex(arr):
    return magicIndex(arr, 0, len(arr) - 1)

def magicIndex(arr, start, end):
    if (end < start):
       return -1
    mid = (start + end) / 2
    if (arr[mid] == mid):
        return mid
    if (arr[mid] < mid):
        return magicIndex(arr, mid + 1, end)
    else:
        return magicIndex(arr, start, mid - 1)
