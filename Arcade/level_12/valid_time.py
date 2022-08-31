'''Check if the given string is a correct time representation of the 24-hour clock.'''


def solution(time):
    split_time = time.split(':')
    hour = split_time[0]
    minutes = split_time[1]

    condition_1 = int(hour) in range(0, 24)
    condition_2 = int(minutes) in range(0, 60)
    
    return condition_1 & condition_2
