from ast import AsyncFunctionDef
from graph import Graph

class Project():
    def __init__(self, name):
        self.name = name
        self.children = []
        self.dependencies = 0

    def addNeighbor(self, end):
        if end.name not in self.children:
            self.children.append(end)

    def incrementDepe

def buildGraph(projects, dependencies):
    g = Graph()
    for p in projects:
        Graph.add(p)
    for d in dependencies:
        