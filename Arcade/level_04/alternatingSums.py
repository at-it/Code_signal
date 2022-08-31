'''Several people are standing in a row and need to be divided into two teams. 
The first person goes into team 1, the second goes into team 2, the third goes into team 1 again,
the fourth into team 2, and so on.'''

a = [50, 60, 60, 45, 70]

def solution(a):
    team_1 = [x for i, x in enumerate(a) if i % 2 == 0]
    team_2 = [x for i, x in enumerate(a) if i % 2 != 0]
    return [sum(team_1), sum(team_2)]

print(solution(a))

# smarter solution using slicers only
def solution_2(a):

    return [sum(a[::2]),sum(a[1::2])]