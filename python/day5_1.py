import re


def _get_input():
    with open('./input/day5.txt', 'r') as data:
        return (cal for cal in data.readlines())
    

def _get_stacks_data(data):
    
    stack_data = []
    for d in data:
        if d == '\n': break
        row = re.split('(.{3})\s', d.rstrip('\n'))
        stack_row = [x[1] for x in row if len(x)==3]
        stack_data.append(stack_row)
        
    return stack_data
    

def _create_stacks(data):
    length = data.pop()
    values = ['' for x in length]
    keys = [str(x) for x in range(1,len(length)+1)]
    stacks = dict(zip(keys, values))
    
    for row in data[::-1]:
        for i, crate in enumerate(row):
            stacks[str(i+1)] += crate if crate.isalpha() else ''
    
    return stacks
    

def _move_stacks(stacks, data, order):
    for move in data:
        num, stack1, stack2 = re.findall('(\d+)', move)
        stacks[stack2] += stacks[stack1][-int(num):][::order]
        stacks[stack1] = stacks[stack1][:-int(num)]    
          
    return ''.join([v[-1] for v in stacks.values() if len(v) != 0])


def main(order):
    data = _get_input()
    stack_data = _get_stacks_data(data)
    stacks = _create_stacks(stack_data)
    result = _move_stacks(stacks, data, order)

    return result
    
if __name__ == '__main__':    
    main(-1)
