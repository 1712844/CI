from unicodedata import name
from StackAndQueue.queue import Queue

import enum

class STATE(enum.Enum):
    UNVISITED = "UNVISITED"
    VISITED = "VISITED"
    VISITING = "VISITING"

class Node():
    def __init__(self, name):
        self.name = name
        self.state = None
        self.children = []

    def getAdjacent(self):
        if self.children is not None:
            return self.children
        
class Graph():
    def __init__(self):
        self.nodes = []

    def add(self, node):
        if node is not None:
            self.append(node) 

    def addEdge(self, first, second):
        for n in self.nodes:
            if first == n.name:
                n.append(second)

    def getNodes(self):
        return self.nodes       

def search(g, start, end):
    if start == end:
        return True
    q = Queue()
    for node in g.getNodes:
        node.state = STATE.UNVISITED
    start.state = STATE.VISITING
    q.add(start)
    u = None
    while(not q.isEmpty):
        u = q.remove()
        if (u is not None):
            for node in u.getAdjacent():
                if node.state == STATE.UNVISITED:
                    if (node == end):
                        return True
                    else:
                        node.state = STATE.VISITING
                        q.add(node)
        u.state = STATE.VISITED
    return False


