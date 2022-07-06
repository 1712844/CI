from operator import rshift
import re
import sys
from unittest import result


def updateBits(n, m, i ,j):
    allOnes = ~0 #11111111
    left = allOnes << (j+1) #11000000
    right = ((1 << i) - 1)  #     011
    mask = left | right     #11000011
    n_cleared = n & mask    #
    m_shifted = m << i 
    return n_cleared | m_shifted

def binaryToSring(double):
    if double >= 1 | double <= 0:
        return "ERROR"
    result = ""
    result+="."
    while (double > 0):
        if (len(result) > 32):
            return "ERROR"
        r = double * 2
        if (r >= 1):
            result+="1"
            double = r - 1
        else:
            result+="0"
            double = r
    return result

def flipBit(a):
    if ~a == 0:
        return sys.getsizeof(int)
    current = 0
    prev = 0
    maxLength = 1
    while (a != 0):
        if a & 1 == 1:
            current+=1
        else:
            if a & 1 == 1:
                prev = 0 if a & 2 == 0 else current
                current = 0
        maxLength = max(current + prev + 1, maxLength)
        a >> 1
    return maxLength

def bitSwapRequired(a, b):
    count = 0
    c = a ^ b
    while (c != 0):
        count += c & 1
        c >> 1
    return count
                