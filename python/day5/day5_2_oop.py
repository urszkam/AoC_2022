import re
from classes import Reader, Stack

    
def main():
    file = Reader('./input/day5.txt')
    file.read()
    iterator = iter(file.data)

    crates = []
    for line in iterator:
        if line == '\n': 
            break
        
        line = re.split('(.{3})\s', line.rstrip('\n'))
        line = [x[1] for x in line if len(x) == 3]
        crates.append(line)
     
    for name in crates.pop():
        obj = Stack(name)
        
    for line in crates[::-1]:
        for i, crate in enumerate(line, start=1):
            if crate != ' ':
                Stack.stack_dict[i].push(crate, reversed=False)
    
    for line in iterator:
        num, stack1, stack2 = list(map(int, re.findall('(\d+)', line)))
        Stack.move(stack1, stack2, num, reversed=False)
        
    Stack.peek_all()
    
    
if __name__ == "__main__":
    main()
    