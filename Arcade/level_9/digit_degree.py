'''Let's define digit degree of some positive integer as the number of times we need to replace this number 
with the sum of its digits until we get to a one digit number.

Given an integer, find its digit degree.'''

n = 91

def solution(n):
    counter = 0
    while len(str(n)) > 1:
        n = sum_digits(n)
        counter += 1
    return counter

def sum_digits(n):
    return sum([int(x) for x in str(n)])

print(solution(n))