'''You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. 
You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.'''

input_array = [5, 3, 6, 7, 9]


def solution(input_array):
    sorted_array = sorted(input_array)
    starting_point = 0
    obstacle_hit = True
    min_jump_length = 2

    while obstacle_hit:
        for i in range(len(sorted_array)):
            if (sorted_array[i] - starting_point) % min_jump_length == 0:
                min_jump_length += 1
                obstacle_hit = True
                break
            obstacle_hit = False

    return min_jump_length

print(solution(input_array))
