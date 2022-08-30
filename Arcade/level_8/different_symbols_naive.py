'''Given a string, find the number of different characters in it.'''

s = "cabca"

def solution(s):
    return len(set(s))

print(solution(s))