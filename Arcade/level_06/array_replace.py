'''Given an array of integers, replace all the occurrences of elem_to_replace with substitution_elem.'''

def solution(input_array, elem_to_replace, substition_elem):
    return [substition_elem if x == elem_to_replace else x for x in input_array]


    