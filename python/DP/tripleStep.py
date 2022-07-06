from tkinter import N


def tripleStep(n):
    memo = [None] * (n + 1)
    return tripleStep

def tripleStep(n, memo):
    if n < 1:
        return 1
    if n == 1:
        return 0
    if memo[n] == None:
        memo[n] == tripleStep(n-1, memo) + tripleStep(n-2, memo) + tripleStep(n-3, memo)
    return memo[n]
    