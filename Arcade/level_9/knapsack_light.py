'''You found two items in a treasure chest! The first item weighs weight1 and is worth value1 
and the second item weighs weight2 and is worth value2. 

What is the total maximum value of the items you can take with you, assuming that your max weight capacity is maxW 
and you can't come back for the items later?

Note that there are only two items and you can't bring more than one item of each type, 
i.e. you can't take two first items or two second items.'''

value_1 = 15
value_2 = 20
weight_1 = 2
weigth_2 = 3
max_w = 2

def solution(value_1, weight_1, value_2, weigth_2, max_w):
    treasures = {'weight': [weight_1, weigth_2], 'value': [value_1, value_2]}
    
    # cannot take anything
    if treasures['weight'][0] > max_w and treasures['weight'][1] > max_w:
        return 0

    # taking both
    if sum(treasures['weight']) <= max_w:
        return sum(treasures['value'])
    
    # taking one, but more expensive
    elif treasures['weight'][0] and treasures['weight'][1] <= max_w:
        return max(treasures['value'])

    # taking what is feasible
    elif treasures['weight'][0] <= max_w:
            return treasures['value'][0]
    
    elif treasures['weight'][1] <= max_w:
            return treasures['value'][1]

    # too heavy
    else:
        return 0

print(solution(value_1, weight_1, value_2, weigth_2, max_w))

# sweet and plain
def solution(value_1, weight_1, value_2, weigth_2, max_w):
    return max(int(weight_1 <= max_w) * value_1, int(weigth_2 <= max_w) * value_2, int(weight_1 + weigth_2 <= max_w)*(value_1 + value_2))