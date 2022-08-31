'''Given a string, output its longest prefix which contains only digits.'''

import re

def solution(input_string):
    return max(re.findall(r'(^[0-9]*)', input_string))
