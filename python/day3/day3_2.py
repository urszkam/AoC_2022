import re
from string import ascii_uppercase, ascii_lowercase


def _get_input():
    with open('./input/day3.txt', 'r') as data:
        return  data.readlines()
    
    
def get_priorities():
    components = _get_input()
    total = 0
    chars = ascii_lowercase + ascii_uppercase
    
    for i in range(0, len(components), 3):
        item = set(components[i]).intersection(
            set(components[i + 1]).intersection(components[i + 2])
        )
        item = re.sub("\n", "", "".join(item))

        total += chars.index(item) + 1

    return total
