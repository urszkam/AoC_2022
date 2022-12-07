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
    sizes = []
    
    for directory in dirs.keys():
        size_sum = sum([v for k,v in dirs.items() if k.startswith(directory)])
        sizes.append(size_sum if size_sum <= 100000 else 0)

    return sum(sizes)
        

if __name__ == '__main__':
    add_sizes()


