"""After becoming famous, the CodeBots decided to move into a new building together. 
Each of the rooms has a different cost, and some of them are free, but there's a rumour that all the free rooms are haunted! 
Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

Given matrix, a rectangular matrix of integers, where each value represents the cost of the room,
your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0)."""


matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]


def solution(matrix):
    no_of_rows = len(matrix)
    no_of_cols = len(matrix[0])

    result = 0

    for i in range(no_of_cols):
        for j in range(no_of_rows):
            if matrix[j][i] == 0:
                break
            result += matrix[j][i]
    return result


print(solution(matrix))
