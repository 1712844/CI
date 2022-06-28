from graph import Graph, STATE

class Project():
    def __init__(self, name):
        self.name = name
        self.children = []
        self.dependencies = 0
        self.nameMap = {}
        self.state = STATE.UNVISITED

    def addNeighbor(self, end):
        if self.nameMap[end.name] == None:
            self.children.append(end)
            self.nameMap[end.name] = end
            end.incrementDependencies()

    def incrementDepedencies(self):
        self.dependencies+=1

    def decrementDepedencies(self):
        self.dependencies-=1


class Graph():
    def __init__(self):
        self.projects = []
        self.nameMap = {}
        
    def getOrCreateNode(self, name):
        if self.nameMap.get[name] == None:
            proj = Project(name)
            self.nameMap[name] = proj
            self.projects.append(proj)
        return self.nameMap[name]

    def addEdge(self, firstName, secondName):
        first = self.getOrCreateNode(firstName)
        second = self.getOrCreateNode(secondName)
        first.addNeighbor(second)
            

def findBuildOrder(projects, dependencies):
    graph = buildGraph(projects, dependencies)
    return orderProjects(graph.projects)

def buildGraph(projects, dependencies):
    g = Graph()
    for p in projects:
        Graph.add(p)
    for d in dependencies:
        firstName = d[0]
        secondName = d[1]
        g.addEdge(firstName, secondName)
    return g

def addIndependentProject(order, projects, offset):
    for p in projects:
        if p.dependencies == 0:
            order[offset] = p
            offset+=1r
    return order

def orderProjects(projects):
    order = []
    toBeProcessed = 0
    endOfList = addIndependentProject(order, projects, 0)
    while(toBeProcessed < len(order)):
        cur = projects[toBeProcessed]
    
        if (cur == None):
            return None
        children = cur.children
    
        for c in children:
            c.decrementDependencies()
    
        endOfList = addIndependentProject(order, children, endOfList)
        toBeProcessed+=1

    return order

def orderProjects2(projects):
    order = []
    for p in projects:
        if p.state == STATE.UNVISITED:
            if not doDFS(p, order):
                return None
    return order

def doDFS(project, order):
    if project.state == STATE.VISITED:
        return False
    if project.state == STATE.UNVISITED:
        project.state = STATE.VISITING
        for c in project.children:
            if (not doDFS(c, order)):
                return False
        project.state = STATE.VISITED
        order.append(project)
    return True
    

