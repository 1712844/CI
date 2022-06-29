def allSequences(node):
    result = []

    if node == None:
        result.append([])
        return result
    
    prefix = []
    prefix.append(node.data)

    leftSeq = allSequences(node.left)
    rightSeq = allSequences(node.right)

    for left in leftSeq:
        for right in rightSeq:
            weaved = []

def weaveLists(first, second, results, prefix):
    if len(first) ==0 or len(second) == 0:
        result = prefix
        result.add(first)
        result.add(second)
        results.add(result)
        return

    headFirst = first.removeFirst();
    prefix.addLast(headFirst); 

    weaveLists(first, second, results, prefix);
    prefix.removeLast();
    first.addFirst(headFirst);

    headSecond = second.removeFirst();
    prefix.addLast(headSecond);
    weaveLists(first, second, results, prefix);
    prefix.removeLast();
    second.addFirst(headSecond);
