"""Ticket numbers usually consist of an even number of digits. 
A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half."""


def solution(n):
    str_n = str(n)
    h1_len = int(len(str_n)/2)
    h2_len = len(str_n) - h1_len
    h1 = str_n[:h1_len]
    h2 = str_n[h2_len:]

    sum_h1 = sum([int(x) for x in h1])
    sum_h2 = sum([int(y) for y in h2])
    return sum_h1 == sum_h2

print(solution(1230))