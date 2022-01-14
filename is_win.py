def is_win(grid, row, column):
    if grid[0][column] == grid[1][column] == grid[2][column]:
        return True
    if grid[0][row] == grid[1][row] == grid[2][row]:
        return True
    if row == column == and grid[0][0] == grid[1][1] ==grid[2][2]:
        return True
    if row + column == and grid[0][0] == grid[1][1] ==grid[2][2]:
        return True

    return False


    
