def searchRotation(array, low, high, value):
    if high < low:
        return -1
    mid = (high + low) / 2
    if value == array[mid]:
        return array[mid]
    if (array[low] < array[mid]):
        if array[low] <= value & value < array[mid]:
            return searchRotation(array, low, mid - 1, value)
        else:
            return searchRotation(array, mid + 1, high, value)
    if (array[high] > array[mid]):
        if array[mid] < value & value <= array[high]:
            return searchRotation(array, low + 1, high, value)
        else:
            return searchRotation(array, low, mid - 1, value)
    if array[low] == array[mid]:
        if array[mid] != array[high]:
            return searchRotation(array, low + 1, high, value)
        else:
            result = searchRotation(array, low, mid - 1, value)
            if (result == -1):
                return searchRotation(array, mid + 1, high, value)
            else:
                return result
    return -1