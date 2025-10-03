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
    strings = []
    letters = [chr(ord("a") + i) for i in range(26)]
    for i in range(num):
        strings.append(''.join(random.choice(letters) for _ in range(length)))
    return strings