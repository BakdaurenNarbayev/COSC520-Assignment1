# String Generation

import random

def generate_strings(num, length = 10):
    '''
        Generate num number of strings with the set lenght
        num : int
            number of strings
        length : int
            length of each string
    '''
    strings = set() # no duplicates
    letters = [chr(ord("a") + i) for i in range(26)]

    while len(strings) < num:
        s = ''.join(random.choice(letters) for _ in range(length))
        strings.add(s)

    return list(strings)