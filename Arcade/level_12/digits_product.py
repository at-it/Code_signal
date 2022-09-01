'''Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. 
If there is no such integer, return -1 instead.'''


product = 12

# naive solution, computentionally heavy
def solution(product):

    # catching edge case
    if product == 0:
        return 10

    # catching others cases
    for i in range(10000):
        result = 1
        for j in str(i):
            result *= int(j)
        if result == product: 
            return i
    return -1


solution(product)

# alternative, much faster
def solution_2(product):
    # catching edge cases
    if product == 0:
        return 10
    elif product == 1:
        return 1
    
    numbers = []

    while 1 < product:
        for digit in range(9, 1, -1):
            if product % digit == 0:
                product /= digit
                numbers.append(digit)
                break
        else:
            return -1

    return int(''.join(map(str, sorted(numbers))))
