'''You're given three integers, a, b and c. It is guaranteed that two of these integers are equal to each other. What is the value of the third integer?'''


def solution(a, b, c):

    if a == b:
        return c
    elif a == c:
        return b
    else:
        return a
        
def solution_2(a, b, c):
    return a ^ b ^ c

def solution_3(a, b, c):
    return c if a == b else a + b - c