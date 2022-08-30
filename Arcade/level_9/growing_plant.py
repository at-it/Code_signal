'''Caring for a plant can be hard work, but since you tend to it regularly, you have a plant that grows consistently. 
Each day, its height increases by a fixed amount represented by the integer upSpeed. 
But due to lack of sunlight, the plant decreases in height every night, by an amount represented by downSpeed.

Since you grew the plant from a seed, it started at height 0 initially. Given an integer desiredHeight, 
your task is to find how many days it'll take for the plant to reach this height.'''

up_speed = 100
down_speed = 10
desired_height = 910

def solution(up_speed, down_speed, desired_height):
    height = 0
    counter = 0
    
    while height < desired_height:
        counter += 1
        height += up_speed
        if height >= desired_height:
            break
        height -= down_speed
        
    return counter

print(solution(up_speed, down_speed, desired_height))
