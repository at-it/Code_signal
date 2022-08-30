'''Find the leftmost digit that occurs in a given string.'''
import re

input_string = "var_1__Int"

def solution(input_string):
    return re.findall(r'[0-9]', input_string)[0]    

print(solution(input_string))