'''Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. 
The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.'''


cell = 'd7'

def solution(cell):

    possible_moves = ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))
    possible_fields = []
    for i in possible_moves:
        cell_col = cell[0]
        cell_row = cell[1]

        final_field_col = chr(ord(cell_col) + i[0])
        final_field_row = int(cell_row) + (i[1])

        if final_field_col in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] and final_field_row in range(1,9):
            possible_fields.append(final_field_col + str(final_field_row))

    return len(possible_fields)

print(solution(cell))