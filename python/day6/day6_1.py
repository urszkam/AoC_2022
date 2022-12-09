def find_sequence(length):
    with open('./input/day6.txt') as data:
        signs = data.read()
    
    # beginning = re.search(r'(?:([A-Za-z])(?!.*\1))', signs)

    for i in range(len(signs) - length):
        if len(set(signs[i : i + length])) == length:
            return i + length


if __name__ == "__main__":
    find_sequence(4)
