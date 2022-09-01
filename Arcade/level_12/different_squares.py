'''Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.'''


matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]


def solution(matrix):

    matrix_cols = len(matrix[0])
    matrix_rows = len(matrix)

    unique_window = []

    for i in range(matrix_rows - 1):
        for j in range(matrix_cols - 1):
            window = [[matrix[i][j], matrix[i][j + 1]],\
                 [matrix[i + 1][j], matrix[i + 1][j + 1]]]
            if window not in unique_window:
                unique_window.append(window)
    return len(unique_window)


print(solution(matrix))