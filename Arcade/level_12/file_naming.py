'''You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names, 
the one which comes later will have an addition to its name in a form of (k), where k is the smallest positive integer 
such that the obtained name is not used yet.

Return an array of names that will be given to the files.'''


def solution(names):

    result = []

    for name in names:
        if name not in result:
            result.append(name)
        else:
            counter = 1
            new_name = name + '(' + str(counter) + ')'
            
            while new_name in result:
                counter += 1
                new_name = name + '(' + str(counter) + ')'

            result.append(new_name)
            
    return result