'''Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between 
any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.'''

# step by step solution 
def solution(n, first_number):
    circle = [x for x in range(n)]
    offset = int(len(circle) / 2)
    final_pos = (first_number + offset) % len(circle)

    return circle[final_pos]

# faster one
def solution_2(n, first_number):
    return (first_number + n/2) % n
