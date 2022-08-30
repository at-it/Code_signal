'''Given a sorted array of integers a, your task is to determine which element of a is closest 
to all other values of a. In other words, find the element x in a, which minimizes the following sum:

abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)
'''

a = [2, 4, 7]
a_2 = [2, 3]

# below would work for not sorted list or when you would need to get value of the distance, not only the element.
def solution(a):
    distances = [calculate_distance(x, a) for x in a]
    min_index = distances.index(min(distances))
    return a[min_index]

def calculate_distance(x, li):
    return sum([abs(x - y) for y in li])

print(solution(a))

# if only element needs to be returned, below is good enough.
def solution_2(a):
    return a[(len(a) - 1)//2]
