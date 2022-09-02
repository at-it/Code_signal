'''Given a divisor and a bound, find the largest integer N such that:

N is divisible by divisor.
N is less than or equal to bound.
N is greater than 0.
It is guaranteed that such a number exists.'''


def solution(divisor, bound):
    i = bound
    while i != 1:
        if i % divisor == 0:
            return i
        i -= 1
    return False

def solution_2(divisor, bound):
    return bound - bound % divisor