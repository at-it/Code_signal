'''In the popular Minesweeper game you have a board with some mines and those cells that don't contain
a mine have a number in it that indicates the total number of mines in the neighboring cells. 
Starting off with some arrangement of mines we want to create a Minesweeper game setup.'''

import copy

matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]


matrix_2 = [[False, False, False],
            [False, False, False]]

matrix_3 = [['true', 'false', 'false', 'true'],
            ['false', 'false', 'true', 'false'],
            ['true', 'true', 'false', 'true']]


def solution(matrix):

    clean_up_matrix(matrix)

    final_matrix = copy.deepcopy(matrix)
    matrix_height = len(final_matrix)
    matrix_width = len(final_matrix[0])

    for col in range(matrix_width):
        for row in range(matrix_height):
            final_matrix[row][col] = calculate_surrounding_mines(
                matrix, row, col)

    return final_matrix


def calculate_surrounding_mines(matrix, row, col):
    temp_matrix = copy.deepcopy(matrix)

    # making sure that we neglect current position
    temp_matrix[row][col] = False

    min_row = max(row - 1, 0)
    max_row = min(min_row + 1, len(temp_matrix)) + 1
    min_col = max(col - 1, 0)
    max_col = min(min_col + 1, len(temp_matrix[0])) + 1

    window = [x[min_col:max_col] for x in temp_matrix[min_row:max_row]]
    window_flat = [s for t in window for s in t]

    return sum(window_flat)


def clean_up_matrix(matrix):
    matrix_height = len(matrix)
    matrix_width = len(matrix[0])
    new_matrix = [True if s == 'true' else False if s ==
        'false' else 'error' for t in matrix for s in t]
    
    pass

print(solution(matrix_3))
