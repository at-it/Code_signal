'''Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.'''

from tkinter import INSIDE


def solution(name):
    is_all_numbers = name.replace('_', '').isalnum()
    starts_with_digit = name[0].isdigit()
    return is_all_numbers and not starts_with_digit

def solution_2(name):
    return name.isidentifier()