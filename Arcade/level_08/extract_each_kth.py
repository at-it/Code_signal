'''Given array of integers, remove each kth element from it.'''

input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
input_array_2 = [1, 1, 1, 1, 1]
input_array_3 = [2, 4, 6, 8, 10]


def solution(input_array, k):
    return [val for i, val in enumerate(input_array, 1) if i % k != 0]


print(solution(input_array, 3))


def solution_2(input_array, k):
    del input_array[k-1::k]
    return input_array
