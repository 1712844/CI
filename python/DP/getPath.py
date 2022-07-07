class Point():
    def __init__(self, row, col):
        self.row = row
        self.col = col

def getPath(maze):
    if maze == None | len(maze) == 0:
        return None
    path = []
    failedPoints = []
    if getPath(maze, len(maze) - 1, len(maze[0]) - 1, failedPoints, path):
        return path
    return None

def getPath(maze, row, col, failedPoints, path):
    if maze[row][col] == None or col < 0 or row < 0:
        return False
    p = Point (row, col)
    if p in failedPoints:
        return False
    isAtOrigin = row == 0 & col == 0
    if (getPath(maze, len(maze), len(maze[0]) - 1, failedPoints, path) or getPath(maze, len(maze) - 1, len(maze[0]), failedPoints, path) or isAtOrigin != False):
        path.append(p)
        return True
    #cache visited point
    failedPoints.append(p)
    return path