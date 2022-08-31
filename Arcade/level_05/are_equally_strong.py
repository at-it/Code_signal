'''Call two arms equally strong if the heaviest weights they each are able to lift are equal.

Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left) 
and so are their weakest arms.'''

from msilib.schema import SelfReg
from unittest import result

your_left = 10
your_right = 15
friends_left = 15
friends_right = 10

def solution (your_left, your_right, friends_left, friends_right):
    
    myself = Person(your_left, your_right)
    friend = Person(friends_left, friends_right)

    if myself.max_strength() == friend.max_strength() and myself.min_strength() == friend.min_strength():
        return True
    else:
        return False
    

class Person:
    def __init__(self, left_arm_strength, right_arm_strength):
        self.left_arm_strength = left_arm_strength
        self.right_arm_strength = right_arm_strength

    def max_strength(self):
        return max(self.left_arm_strength, self.right_arm_strength)

    def min_strength(self):
        return min(self.left_arm_strength, self.right_arm_strength)

# or, way simpler :)

def solution_2(yourLeft, yourRight, friendsLeft, friendsRight):
    return {yourLeft, yourRight} == {friendsLeft, friendsRight}

print(solution(your_left, your_right, friend_left, friend_right))