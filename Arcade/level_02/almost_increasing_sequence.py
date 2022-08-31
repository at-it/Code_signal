"""Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array."""


sequence_1 = [1, 2, 3, 4]
sequence_2 = [6, 1, 3, 4]
sequence_3 = [8, 1, 4, 2]
sequence_4 = [1, 2, 3, 4, 3, 6]
sequence_5 = [1, 3, 2]
sequence_6 = [10, 1, 2, 3, 4, 5]
sequence_7 = [1, 2, 5, 3, 5]
sequence_8 = [1, 2, 3, 4, 6, 2]
sequence_9 = [1, 1]

# my solution
def solution(sequence):

    is_increasing, n = check_if_increasing(sequence)

    if is_increasing or n == len(sequence) - 1 or len(sequence) <=2:
        return True

    new_sequence = sequence[:n] + sequence[n + 1:]
    new_sequence_2 = sequence[:n + 1] + sequence[n + 2:]
   
    if check_if_increasing(new_sequence)[0] == True or check_if_increasing(new_sequence_2)[0] == True:
        return True
    return False


def check_if_increasing(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i] < sequence[i + 1]:
            continue
        else:
            return False, i
    return True, i

print(solution(sequence_9))

# working alternative code
def almostIncreasingSequence(sequence):
    i = 0
    while i < len(sequence) - 1:
        if not sequence[i] < sequence[i + 1]:
            if increasingSequence(sequence[:i] + sequence[i+1:]) or \
                    increasingSequence(sequence[:i+1] + sequence[i+2:]):
                return True
            else:
                return False
        i += 1
    return True


def increasingSequence(sequence):
    for i in range(len(sequence) - 1):
        if not sequence[i] < sequence[i + 1]:
            return False
    return True