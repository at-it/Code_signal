"""Given an array of strings, return another array containing all of its longest strings."""

input_array = ["aba", "aa", "ad", "vcd", "aba"]
input_array_2 = ["enyky", "benyky", "yely","varennyky"]

def solution(input_array):
    word_lenghts = map(lambda x: len(x), input_array)
    max_word_length = max(word_lenghts)
    result = [x for x in input_array if len(x) == max_word_length]
    return result

print(solution(input_array_2))
