'''Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.'''

input_array = [2, 4, 1, 0]
input_array_2 = [10, 11, 13]

def solution(input_array):
    return max([abs(x - y) for x, y in zip(input_array, input_array[1:])])

print(solution(input_array_2))
