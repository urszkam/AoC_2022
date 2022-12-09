def count_trees():
    with open('./input/day8.txt', 'r') as input_data:
        trees = input_data.readlines()
    
    trees_rows = []
    
    for tree in trees:
        trees_int = [int(x) for x in tree.strip()]
        trees_rows.append(trees_int)
    
    trees_columns = list(map(list, zip(*trees_rows)))
    total = 0
    
    for r in range(len(trees_rows)):
        for c in range(len(trees_columns)):
            tree = trees_rows[r][c]

            if c == 0 or r == 0 or c == len(trees_rows) - 1 or r == len(trees_rows) - 1:
                total += 1

            elif (
                tree > max(trees_rows[r][:c])
                or tree > max(trees_rows[r][c + 1 :])
                or tree > max(trees_columns[c][:r])
                or tree > max(trees_columns[c][r + 1 :])
            ):
                total += 1

    return total


if __name__ == "__main__":
    count_trees()
