"""Write a function that reverses characters in (possibly nested) parentheses in the input string."""

import re

input_string_1 = "foo(bar)baz"
input_string_2 = "(bar)"
input_string_3 = "foo(bar)baz(blim)"
input_string_4 = "foo(bar(baz))blim"

def solution(input_string):
    if len(input_string) == 0:
        return input_string
    
    if not ('(' in input_string and ')' in input_string):
        return input_string
        
    word = list(input_string)
    
    while '(' in word or ')' in word:
        word_str = ''.join(word)
        pos_lb = word_str.rfind('(')
        pos_rb = word_str.find(')', pos_lb)
        word_to_reverse = word[pos_lb + 1 :pos_rb]
        reversed_word = word_to_reverse[::-1]
        final_word = word[:pos_lb] + reversed_word + word[pos_rb + 1:]
        word = final_word
        
    return ''.join(final_word)


#regex may not necessarily work here... issue with replacement of all occurances
def solution_2(input_string):
    word_to_reverse = re.findall(r"(?<=\().*?(?=\))", input_string)
    reversed_word = [str(x)[::-1] for x in word_to_reverse]
    result = [re.sub(r'\(.*?\)', word, input_string) for word in reversed_word]
    return result

print(solution(input_string_4)) 