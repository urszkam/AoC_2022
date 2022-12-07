import re
from classes import Reader, Directory


file = Reader('./input/day7.txt')

for command in file.data:
    if command.startswith('$ cd'):
        print(command)
        dir_name = re.search('[\w./]{1,}$', command)
        Directory.change_dir(dir_name.group())
            
    elif re.match('\d+\s[\w.]*', command):
        print(command)
        size, file = re.findall('(\d+)\s([\w.]+)', command.strip())[0]
        Directory.add_file(file, size)
    