'''Given two cells on the standard chess board, determine whether they have the same color or not.'''

cell_1 = "A1"
cell_2 = "C3"

# more step by step
def solution(cell_1, cell_2):

    # Setup board
    board = [chr(letter_num) + str(digit)
             for letter_num in range(65, 73) for digit in range(1, 9)]
    pattern = ['white' if x % 2 != 0 else 'dark' for x in range(8)]
    pattern_2 = ['dark' if x % 2 != 0 else 'white' for x in range(8)]

    full_pattern = []
    for i in range(8):
        if i % 2 == 0:
            full_pattern.extend(pattern)
        else:
            full_pattern.extend(pattern_2)

    full_board = dict(zip(board, full_pattern))
    return full_board[cell_1] == full_board[cell_2]

# much faster
def solution_2(cell_1, cell_2):
    return (ord(cell_1[0]) + int(cell_1[1])) % 2 == (ord(cell_2[0]) + int(cell_2[1])) % 2


print(solution_2('A1', 'C3'))
