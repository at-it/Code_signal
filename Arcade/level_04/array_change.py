'''You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. 
Find the minimal number of moves required to obtain a strictly increasing sequence from the input.'''

input_array = [1, 1, 1]


def solution(input_array):

    counter = 0
    final_array = input_array.copy()
    for i in range(len(final_array) - 1):
        if not final_array[i] < final_array[i + 1]:
            diff = max(abs(final_array[i + 1] - final_array[i]), 0) + 1
            final_array[i + 1] = final_array[i + 1] + diff
            counter += diff
    return counter


print(solution(input_array))
