'''Some phone usage rate may be described as follows:

first minute of a call costs min1 cents,
each minute from the 2nd up to 10th (inclusive) costs min2_10 cents
each minute after 10th costs min11 cents.
You have s cents on your account before the call. What is the duration of the longest call (in minutes rounded down to the nearest integer) you can have?
'''


def solution(min_1, min_2_10, min_1_1, s):
    
    duration = 0
    balance = s - min_1
    
    # first tariff
    if balance >= 0:
        first_tarif_duration = 1
        duration = first_tarif_duration
    else:
         return 0

    # second tariff
    second_tariff_duration = balance // min_2_10

    if second_tariff_duration > 9:
        second_tariff_duration = 9
        second_tariff_cost = 9 * min_2_10
    else:
        return first_tarif_duration + second_tariff_duration

    balance = balance - second_tariff_cost
    duration += second_tariff_duration

    # third tariff

    third_tariff_duration = balance // min_1_1
    duration += third_tariff_duration 

    return duration

# more compact version

def solution(min_1, min_2_10, min_1_1, s):
    if s < min_1:
        return 0
    elif s >= min_1 and s <= min_1 + 9 * min_2_10:
        return 1 + (s - min_1) // min_2_10
    return 10 + (s - min_1 - 9 * min_2_10) // min_1_1