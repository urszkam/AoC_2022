import re
from day4_1 import _get_input


def find_overlaps():
    assignments = _get_input()
    total = 0
    
    for pair in assignments:
        a, b, c, d = list(map(int, re.findall('(\d+)', pair)))
        
        if (c <= b <= d) or (c <= a <=d) \
            or (a <= c <= b) or (a <= d <=b):
             total += 1
        else:
            print(a,b,c,d)

    return total

print(find_overlaps())