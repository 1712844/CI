from StackAndQueue.stack import Stack

def moveDisks(n, origin, buffer, destination):
    if n <= 0:
        return
    moveDisks(n - 1, origin, destination, buffer)
    moveTop(origin, destination)
    moveDisks(n-1, buffer, destination, origin)

def moveTop(origin, t):
    top = origin.pop()
    t.push(top)


