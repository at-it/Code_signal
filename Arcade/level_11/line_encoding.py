'''Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.'''

s = 'aabbbc'


def solution(s):
    chars = []
    counter = []

    chars.append(s[0])
    counter.append(1)

    same_chars = 0
    
    for i in range(1, len(s)):

        if s[i] == s[i - 1]:
            same_chars += 1
            counter[i - same_chars] += 1
        else:
            chars.append(s[i])
            counter.append(1)
   
    return ''.join([y if x == 1 else str(x) + y for x, y in list(zip(counter, chars))])


print(solution(s))
