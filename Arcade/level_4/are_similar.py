'''Two arrays are called similar if one can be obtained from another 
by swapping at most one pair of elements in one of the arrays.'''


a = [1, 2, 3]
b = [1, 2, 3]

a_2 = [1, 2, 3]
b_2 = [2, 1, 3]


def solution(a, b):

    sym_diff = set(a).symmetric_difference(set(b))
    if len(sym_diff) > 1:
        return False

    diff_elements = ([(x, y) for x, y in zip(a, b) if x != y])
    unique_elements = set([s for t in diff_elements for s in t])
    if len(unique_elements) <= 2 and len(diff_elements) <= 2:
        return True
    else:
        return False


print(solution(a_2, b_2))

# alternative from web
def solution(A, B):
    return sorted(A) == sorted(B) and sum([a != b for a, b in zip(A, B)]) <= 2
