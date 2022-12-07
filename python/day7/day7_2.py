import math


def add_sizes():

    with open('./input/day7.txt', 'r') as input_data:
        commands = input_data.readlines()
        
    current = '/'
    dirs = {}
    total = 0
    
    for command in commands[1:]:
        
        if command.startswith('$ cd'):
            dir_name = command.strip().rsplit(' ', 1)[-1]
            
            if current not in dirs.keys():
                dirs[current] = total
                total = 0
            
            if dir_name == '..':
                current = current.rsplit('/', 1)[0]
            
            else:        
                current = f'{current}/{dir_name}'
                
        elif command[0].isdigit():
            size = command.split(' ', 1)[0]
            total += int(size)
            
    dirs[current] = total
    
    total_space = 70000000
    needed_space = 30000000
    current_space = total_space - sum(dirs.values())
    space_to_free = needed_space - current_space
    
    min_diff = math.inf
    
    for directory in dirs.keys():
        size_sum = sum([v for k,v in dirs.items() if k.startswith(directory)])

        if space_to_free <= size_sum and \
            abs(space_to_free - size_sum) < min_diff:
                min_diff = abs(space_to_free - size_sum)
                min_size = size_sum

    print(space_to_free, min_size)
    

if __name__ == '__main__':
    add_sizes()
    