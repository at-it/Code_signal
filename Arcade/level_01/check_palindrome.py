"""Given the string, check if it is a palindrome."""

def solution(inputString):
    reversed_string = inputString[::-1]
    
    if inputString == reversed_string:
        return True
    else:
        return False
