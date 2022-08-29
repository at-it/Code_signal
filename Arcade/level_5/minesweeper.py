'''In the popular Minesweeper game you have a board with some mines and those cells that don't contain
a mine have a number in it that indicates the total number of mines in the neighboring cells. 
Starting off with some arrangement of mines we want to create a Minesweeper game setup.'''

import copy

matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]

matrix_2 = [[False, False, False],
            [False, False, False]]

matrix_3 = [[True, False, False, True],
            [False, False, True, False],
            [True, True, False, True]]


def solution(matrix):

    final_matrix = copy.deepcopy(matrix)
    matrix_height = len(final_matrix)
    matrix_width = len(final_matrix[0])

    for row in range(matrix_height):
        for col in range(matrix_width):
            final_matrix[row][col] = calculate_surrounding_mines(matrix, row, col)

    return final_matrix


def calculate_surrounding_mines(matrix, row, col):

    # setup of moving window
    min_row = max(row - 1, 0)
    max_row = row + 2
    min_col = max(col - 1, 0)
    max_col = col + 2

    window = [x[min_col:max_col] for x in matrix[min_row:max_row]]
    
    # making sure that we neglect current position
    window[row - min_row][col - min_col] = False
    
    # flattenning for summing 
    window_flat = [s for t in window for s in t]

    return sum(window_flat)


print(solution(matrix_3))
