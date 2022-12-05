import re


def _get_input():
    with open('./input/day4.txt', 'r') as data:
        return (cal for cal in data.readlines())
    
    
def find_overlaps():
    assignments = _get_input()
    total = 0
    
    for pair in assignments:
        assign = list(map(int, re.findall('(\d+)', pair)))
        
        if (assign[0] >= assign[2] and assign[1] <= assign[3]) \
         or (assign[0] <= assign[2] and assign[1] >= assign[3]):
             total += 1

    return total

    