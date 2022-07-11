from http import server


def search(strings, low, high, value):
    if low > high:
        return -1
    mid = (low + high) / 2
    if strings[mid] == "":
        left = mid - 1
        right = mid + 1
        while(True):
            if left < low | right > high:
                return -1
            if left >= low & strings[left] != "":
                mid = left
                break
            if right <= high & strings[right] != "":
                mid = right
                break
            left -= 1
            right -= 1
    if strings[mid] == value:
        return strings[mid]
    if strings[mid] > value:
        return search(strings, low, mid - 1, value)
    else:
        return search(strings, mid + 1, high, value)
        