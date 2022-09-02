'''Consider an arithmetic expression of the form a#b=c. 
Check whether it is possible to replace # with one of the four signs: +, -, * or / to obtain a correct expression.'''


def solution(a, b, c):
    # layout: a # b = c
    list_of_signs = ['+', '-', '*', '/']

    for i in list_of_signs:
        expression = eval(f'a {i} b = c')
        if expression:
            return True
    return False

def solution_2(a, b, c):
    return c in (a + b, a - b, a * b, a / b)

