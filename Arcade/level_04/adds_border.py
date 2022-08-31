'''Given a rectangular matrix of characters, add a border of asterisks(*) to it.'''

picture = ["abc",
           "ded"]

def solution(picture):
    width = len(picture[0]) + 2
    height = len(picture) + 2

    for i in range(len(picture)):
        picture[i] = '*' + picture[i] + '*'

    picture.insert(0, '*'*width)
    picture.insert(height, '*'*width)
    
    return picture
    

print(solution(picture))
