"""Given an array of strings, return another array containing all of its longest strings."""

s1 = "aabcc"
s2 = "adcaa"

def solution(s1, s2):
    common_chars = set(s1).intersection(set(s2))
    result = 0

    for letter in common_chars:
        s1_count = s1.count(letter)
        s2_count = s2.count(letter)
        result += min([s1_count, s2_count])

    return result

print(solution(s1, s2))