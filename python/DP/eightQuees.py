GRID_SIZE = 8

class compromisedPos():
    def __init__(self, r, c):
        self.row = r
        self.column = c

def placeQueens(row, columns, results):
    if row >= GRID_SIZE:
        results.append(columns)
    else:
        for c in range(GRID_SIZE):
            if (checkValid(columns, row, c)):
                columns[row] = c
                placeQueens(columns, row + 1, results)

def checkValid(columns, row, col):
    for r in range(row):
        if columns[r] == col:
            return False
        
        colDistance = abs(columns[r] - col)
        rowDistance = row - r
        if colDistance == rowDistance:
            return False
    return True
    

