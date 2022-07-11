from json import tool
from turtle import right


def countEval(str, result):
    if len(str) == 0:
        return 0
    if len(str) == 1:
        return 1 if str == "1" else  0

    ways = 0

    for i in range(str):
        c = str[i]
        leftStr = str[:i]
        rightStr = str[i+1:]
        leftTrue = countEval(leftStr, True)
        leftFalse = countEval(leftStr, False)
        rightTrue = countEval(rightStr, True)
        rightFalse = countEval(rightStr, False)
        totalWays = (leftTrue + leftFalse) * (rightFalse + rightTrue)
        totalTrue = 0
        if (c == "&"):
            totalTrue = leftTrue * rightTrue
        if (c == "^"):
            totalTrue = leftTrue * rightFalse + leftFalse * rightTrue
        if (c == "|"):
            totalTrue = leftTrue * rightTrue + leftFalse * rightTrue + leftTrue * rightFalse
        
        subWays = result if totalWays - totalTrue else totalTrue
        ways += subWays
    return ways
