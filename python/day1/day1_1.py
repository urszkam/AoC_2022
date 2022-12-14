import re


def _get_input():
    with open('./input/day1.txt', 'r') as data:
        return (cal for cal in data.readlines())
    
    
def count_max_calories():
    calories = _get_input()
    cal_max = cal_total = 0
    
    for cal in calories:
        if cal == "\n":
            cal_max = max(cal_max, cal_total)
            cal_total = 0
        elif re.match('\d+\n', cal):
            cal_total += int((re.search('^(\d+)\n$', cal)).group())
    return cal_max
