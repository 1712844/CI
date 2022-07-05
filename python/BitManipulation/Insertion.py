def updateBits(n, m, i ,j):
    allOnes = ~0 #11111111
    left = allOnes << (j+1) #11000000
    right = ((1 << i) - 1)  #     011
    mask = left | right     #11000011
    n_cleared = n & mask    #
    m_shifted = m << i 
    return n_cleared | m_shifted

def 