'''Given the positions of a white bishop and a black pawn on the standard chess board, 
determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement.'''


def solution(bishop, pawn):
    ''' this comes from the fact that in order to capture pawn in one move, bishop needs to be on the diagonal.
    Meaning the slope of the difference between two positions needs to be 1.'''

    return abs(int(bishop[1]) - int(pawn[1])) == abs(ord(bishop[0]) - ord(pawn[0]))