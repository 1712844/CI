import numpy as np

class Solution(object):
    def isUniqueChars(self, s):
        if s.length > 128:
            return False
        a = np.array[s.length]
        