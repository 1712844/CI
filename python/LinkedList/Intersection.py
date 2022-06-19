def findIntersection(list1, list2):
    if list1 is None or list2 is None:
        return None
    last1, len1 = getLastNodeAndLength(list1)
    last2, len2 = getLastNodeAndLength(list2)
    if (last1 != last2):
        return None
    longer = list1 if len1 > len2 else list2
    shorter = list1 if len1 < len2 else list2

    longer = getKthNode(longer, )

    if (longer != shorter):
        longer = longer.next
        shorter = shorter.next

    return longer

def getKthNode(list1, k): 
    pos = 0
    cur = list1
    while(pos < k):
        cur = cur.next
        pos+=1
    return cur

def getLastNodeAndLength(list):
    cur = list
    len = 0
    while(cur is not None):
        cur = cur.next
        len+=1
    return cur, len