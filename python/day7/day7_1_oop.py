import re
from classes import Reader, Directory


def sum_file_sizes():
    file = Reader('./input/day7.txt')
    dirs = {}

    for command in file.data:
        if command.startswith('$ cd'):
            search_result = re.search('[\w./]{1,}$', command.strip())
            dir_name = search_result.group()
            full_dir = Directory.find_directory(dir_name)
            if dir_name == '..':
                Directory.go_up()
                
            elif full_dir in dirs.keys():
                Directory.go_down(dirs[full_dir])
                
            else:
                dir_obj = Directory(full_dir)
                dirs.update({dir_obj.name: dir_obj})
                Directory.go_down(dir_obj)
                
        elif re.match('\d+\s[\w.]*', command):
            size, file = re.findall('(\d+)\s([\w.]+)', command.strip())[0]
            Directory.add_file(file, size)
        
    sizes = {}
    for k,directory in dirs.items():
        dir_size = directory.count_dir_size()
        sizes.update({k: dir_size})
    
    result = sum([x for x in sizes.values() if x <= 100000])
    print(sizes)
    
if __name__ == "__main__":
    sum_file_sizes()
    