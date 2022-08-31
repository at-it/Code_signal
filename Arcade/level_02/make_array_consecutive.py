"""Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size.
 Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1.
 He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed."""


def solution(statues):
    sorted_statues = sorted(statues)
    counter = 0

    for i in range(len(sorted_statues) - 1):

        diff_between_adjacent_elements = sorted_statues[i + 1] - sorted_statues[i]
        if diff_between_adjacent_elements > 1:
            counter += diff_between_adjacent_elements - 1

    return counter
