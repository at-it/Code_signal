'''Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column, 
each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.'''


grid = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]

checklist = [x for x in range(1, 10)]


def solution(grid):
    if check_box(grid) and check_rows(grid) and check_cols(grid):
        return True
    else:
        return False


def check_rows(grid):
    for i in range(len(grid)):
        if set(grid[i]) == set(checklist):
            continue
        else:
            return False
    return True


def check_cols(grid):
    # this is effectively swapping columns to rows, hence previous method can be used.
    cols = [x for x in zip(*grid)]
    return check_rows(cols)


def check_box(grid):

    step = 3
    for row in range(0, len(grid), step):
        for col in range(0, len(grid[0]), step):

            window_rows = grid[row:row+step]
            window = [x[col:col+step] for x in window_rows]
            
            flat_list = [subelement for element in window for subelement in element]

            if set(flat_list) == set(checklist):
                continue
            else:
                return False  
    return True


print(solution(grid))
