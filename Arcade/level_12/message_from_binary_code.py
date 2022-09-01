'''You are taking part in an Escape Room challenge designed specifically for programmers. In your efforts to find a clue, 
you've found a binary code written on the wall behind a vase, and realized that it must be an encrypted message. 
After some thought, your first guess is that each consecutive 8 bits of the code stand for the character with the corresponding extended ASCII code.

Assuming that your hunch is correct, decode the message.'''


def solution(code):
    return "".join([chr(int(code[8*i:8*i+8],2)) for i in range(len(code)//8)])

def solution_2(code):
    n = int(code, 2)
    result = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    return result
