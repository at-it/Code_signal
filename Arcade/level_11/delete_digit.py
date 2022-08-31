'''Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.'''


n = 1001


def solution(n):
    sums = []
    list_of_str_digits = [x for x in str(n)]
    for i in range(len(list_of_str_digits)):
        sums.append(list_of_str_digits[:i] + list_of_str_digits[i + 1:])

    list_of_digits = [int(''.join(x)) for x in sums]

    return max(list_of_digits)

print(solution(n))
