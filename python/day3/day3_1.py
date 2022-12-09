from string import ascii_uppercase, ascii_lowercase


def _get_input():
    with open('./input/day3.txt', 'r') as data:
        return (cal for cal in data.readlines())
    
    
def get_priorities():
    components = _get_input()
    total = 0
    chars = ascii_lowercase + ascii_uppercase
    
    for component in components:
        component = component.strip('\n')
        
        mid = len(component) // 2
        item = set(component[:mid]).intersection(set(component[mid:]))
        item = item.pop()
        
        
        total += chars.index(item) + 1
    return total
