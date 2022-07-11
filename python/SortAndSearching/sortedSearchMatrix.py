def search(matrix, value):
    row = 0
    col = len(matrix[0])-1
    while(row < len(matrix) & col > 0):
        if matrix[row][col] == value:
            return True
        if matrix[row][col] > value:
            col -= 1
        else:
            row += 1
    return True