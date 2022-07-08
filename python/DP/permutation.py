from itertools import permutations


def getPermutations(str):
    if str == None:
        return None
    permutations = []
    if (len(str) == 0):
        permutations.append("")
        return permutations
    firstChar = str[0]
    permutations = getPermutations(str[1:])
    for l in list:
        for pos in len(l):
            newPerm = insertCharAt(l, firstChar, pos)
            permutations.append(newPerm)
    return permutations

def insertCharAt(word, c, pos):
    firstSubString = word[0:pos]
    secondSubString = word[pos:len(word)]
    return firstSubString + c + secondSubString

#n-1 substrings
def getPermutations2(remainder):
    if str == None:
        return None
    permutations = []
    if len(str) == 0:
        permutations.append("")
        return permutations
    for i in range(len(remainder)):
        begin = remainder[:i]
        end = remainder[i + 1:]
        partials = getPermutations2(begin + end)
        for p in partials:
            permutations.append(remainder[i] + p)
    return permutations

def getPermutations3(prefix, remainder, result):
    if len(remainder) == 0:
        result.append(prefix)
    for i in range(len(remainder)):
        first = remainder[:i]
        second = remainder[i+1:]
        c = remainder[i]
        getPermutations3(c, first + second, result)