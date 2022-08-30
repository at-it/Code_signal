'''Given array of integers, find the maximal possible sum of some of its k consecutive elements.'''

input_array = [2, 3, 5, 1, 6]

def solution(input_array, k):
    sum_elements = sum(input_array[0:k])
    result = sum_elements
    for i in range(1, len(input_array) - k + 1):
        sum_elements = sum_elements - input_array[i - 1] + input_array[i + k - 1]
        result = max(result, sum_elements)
    return result

# although works, it's performance is slower than alternative
def solution_2(input_array, k):
    return max([sum(input_array[i:i+k]) for i in range(len(input_array))])

print(solution(input_array, 3))