'''Define a word as a sequence of consecutive English letters. Find the longest word from the given string.'''


import re

text = "Not not Not not Not not"

def solution(text):

    list_of_words = re.split(r'[^a-zA-Z]', text)
    length_list = list(map(lambda x: len(x), list_of_words))
    index_of_longest_word = length_list.index(max(length_list))

    return list_of_words[index_of_longest_word]

print(solution(text))

#alternative solution, more compact
def solution_2(text):
    return max(re.split('[^a-zA-Z]', text), key=len)
