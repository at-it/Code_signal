'''Given a string, your task is to replace each of its characters by the next one in the English alphabet; 
i.e. replace a with b, replace b with c, etc (z would be replaced by a)'''

input_string = 'crazy'

# more step by step
def solution (input_string):
    list_of_strings = [x for x in input_string]
    char_numbers = list(map(lambda x: ord(x), list_of_strings))

    new_char_numbers = []

    for i in char_numbers:
        
        if i == 122:
            char_num = 97
        else:
            char_num = i + 1

        new_char_numbers.append(char_num)
    
    new_word = ''.join([chr(x) for x in new_char_numbers])
    return new_word

print(solution(input_string))

# more compact
def solution_2(input_string):
    return ''.join([chr(ord(x) + 1) if x != 'z' else 'a' for x in input_string])

print(solution_2(input_string))
