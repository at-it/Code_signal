'''Given an array of equal-length strings, you'd like to know if it's possible to rearrange the order of the elements 
in such a way that each consecutive pair of strings differ by exactly one character. Return true if it's possible, and false if not.

Note: You're only rearranging the order of the strings, not the order of the letters within the strings!'''

from itertools import permutations

input_array = ["aba", "bbb", "bab"]
input_array_2 = ["ab", "bb", "aa"]
input_array_3 = ["aba", "bbb", "bab"]


def solution(input_array):
    all_perms = list(permutations(input_array))
    for perm in all_perms:
        counter = 0
        for element in range(len(perm) - 1):
            if is_diff_by_one_char(perm[element], perm[element + 1]) != True:
                break
            counter += 1
            if counter == len(perm) - 1:
                return True
    return False


def is_diff_by_one_char_2(string_1, string_2):
    return sum([a[0] != a[1] for a in zip(string_1, string_2)])


print(solution(input_array))

# actually proven to be a slower one in cases of strings around ~30 letters
def is_diff_by_one_char(string_1, string_2):
    counter = 0
    string_1_elements = [x for x in string_1]
    string_2_elements = [x for x in string_2]

    for i in range(len(string_1_elements)):
        if string_1_elements[i] != string_2_elements[i]:
            counter += 1
            continue
        if counter > 1:
            return False

    return counter == 1
