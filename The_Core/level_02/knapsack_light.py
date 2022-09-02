'''You found two items in a treasure chest! The first item weighs weight1 and is worth value1, 
and the second item weighs weight2 and is worth value2. What is the total maximum value of the items you can take with you, 
assuming that your max weight capacity is maxW and you can't come back for the items later?

Note that there are only two items and you can't bring more than one item of each type, i.e. you can't take two first items or two second items.'''


def solution(value_1, weight_1, value_2, weight_2, max_w):
    return max(int(weight_1 <= max_w) * value_1, int(weight_2 <= max_w) * value_2, int(weight_1 + weight_2 <= max_w) * (value_1 + value_2))