'''A string is said to be beautiful if each letter in the string appears at most as many times 
as the previous letter in the alphabet within the string; 

example: b occurs no more times than a; c occurs no more times than b; etc. Note that letter a has no previous letter.

Given a string, check whether it is beautiful.'''

input_string = 'bbc'


def solution(input_string):

    alphabet = [chr(x) for x in range(97, 123)]
    counts = [input_string.count(x) for x in alphabet]
    return counts == sorted(counts, reverse=True)


print(solution(input_string))
