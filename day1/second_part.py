import re
from first_part import _get_input


def add_three_max():
    calories = _get_input()
    cal_total = 0
    max_cal = [0 for x in range(3)]
    
    for cal in calories:
        if cal == '\n':
            if cal_total >= max_cal[0]:
                max_cal[2], max_cal[1], max_cal[0] = max_cal[1], max_cal[0], cal_total
            elif cal_total >= max_cal[1]:
                max_cal[2], max_cal[1] = max_cal[1], cal_total
            elif cal_total > max_cal[2]:
                max_cal[2] = cal_total
            cal_total = 0
        elif re.match('\d+\n$', cal):
            cal_total += int((re.search('^(\d+)\n$', cal)).group())
            
    return sum(max_cal)

if __name__ == '__main__':
    add_three_max()