def getParens(remaining):
    set = []
    if remaining == 0:
        set.append("")
    else:
        set = getParens(remaining - 1)
        for s in set:
            for i in range(len(s)):
                if s[i] == "(":
                    newPattern = insertParens(s, i)
                    set.append(s)
            set.append("()" + s)
    return set


def insertParens(str, leftPos):
    leftStr = str[:leftPos]
    rightStr = str[leftPos:]
    return leftStr + "()" + rightStr