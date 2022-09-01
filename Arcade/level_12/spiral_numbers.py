'''Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.'''


n = 3

def solution(n):

    # initialize matrix with zeros
    matrix = [[0] * n for x in range(n)]

    i = 0
    j = 0
    di = 0
    dj = 1

    for matrix[i][j] in range(1, n*n + 1):
        # condition checked in order to refer to first position of the matrix, meaning [0][0].
        # if this is met, it means we have gone through whole row and need to change direction.

        if matrix[(i+di) % n][(j+dj) % n]:
            di, dj = dj, -di
        i += di
        j += dj
    return matrix

print(solution(n))
