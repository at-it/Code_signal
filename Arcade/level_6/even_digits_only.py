'''Check if all digits of a give integer are even.'''

def solution(n):
    list_of_ints = [int(x) for x in str(n)]
    check_if_even = all([True if x % 2 == 0 else False for x in list_of_ints])
    return check_if_even
