'''Given a string, find out if it satisfies the IPv4 address naming rules.'''

input_string = "172.16.254.1"
input_string_2 = "172.316.254.1"

def solution(input_string):
    list_of_numbers = input_string.split('.')
    
    is_between_0_and_255 = all(x in list(map(str, range(0,256))) for x in list_of_numbers)
    contains_4_digits = len(list_of_numbers) == 4
    
    if contains_4_digits and is_between_0_and_255:
        return True
    else:
        return False