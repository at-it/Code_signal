'''Given a string, find out if its characters can be rearranged to form a palindrome.'''

input_string = 'aabb'

def solution(input_string):
    
    no_of_odd_chars = len([x for x in set(input_string) if input_string.count(x) % 2 != 0])

    return no_of_odd_chars <= 1
