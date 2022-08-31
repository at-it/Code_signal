'''Elections are in progress!

Given an array of the numbers of votes given to each of the candidates so far, and an integer k equal to the number of voters who haven't cast their vote yet, 
find the number of candidates who still have a chance to win the election.

The winner of the election must secure strictly more votes than any other candidate. If two or more candidates receive the same (maximum) number of votes, 
assume there is no winner at all.
'''

k = 3
votes = [2, 3, 5, 2]


# seem to scale better
def solution(votes, k):
    max_votes = max(votes)
    count_max_votes = votes.count(max_votes)
    
    if k == 0 and count_max_votes == 1:
        return 1
    elif k == 0 and count_max_votes != 1:
        return 0
    else:
        return len(list(filter(lambda x: x + k > max_votes, votes)))


# works faster for small examples
def solution_2(votes, k):

    max_votes = max(votes)

    if k == 0 and votes.count(max_votes) == 1:
        return 1
    elif k == 0 and votes.count(max_votes) != 1:
        return 0
    else:
        return len([x for x in votes if x + k > max_votes])


# another alternative
def solution_3(votes, k):
    counter = 0
    max_votes = max(votes)

    if k == 0 and votes.count(max_votes) == 1:
        return 1

    for i in votes:
        if i + k > max_votes:
            counter += 1
    return counter
