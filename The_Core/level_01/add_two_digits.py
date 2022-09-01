'''You are given a two-digit integer n. Return the sum of its digits.'''


def solution(n):
    return sum([int(x) for x in str(n)])
