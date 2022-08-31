'''Given a string, find the shortest possible string which can be achieved by 
adding characters to the end of initial stringto make it a palindrome.'''


s = 'abcdc'

def solution(s):
    
    if s == s[::-1]:
        return s

    i = 0
    substring = s[i:]
    while substring != substring[::-1]:
        i += 1
        substring = s[i:]

    return s + s[i - 1:: -1]

print(solution(s))