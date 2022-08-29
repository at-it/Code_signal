"""Some people are standing in a row in a park. There are trees between them which cannot be moved. 
Your task is to rearrange the people by their heights in a non-descending order without moving the trees. 
People can be very tall!"""


a = [-1, 150, 190, 170, -1, -1, 160, 180]

def solution(a):
    sorted_elements = [x for x in sorted(a) if x != -1]

    counter = 0
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = sorted_elements[counter]
            counter += 1
    return a

print(solution(a))