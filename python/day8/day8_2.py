import re


def find_distance(pattern, trees):
    search_result = re.search(pattern, trees)
    return len(trees) \
            if search_result is None  \
            else search_result.start() + 1


def find_max_view():
    with open('./input/day8.txt', 'r') as input_data:
        trees = input_data.readlines()
    
    trees_rows = [tree.strip() for tree in trees]   
    trees_columns = list(map(''.join, list(map(list, zip(*trees_rows)))))

    max_score = 0
     
    for r in range(len(trees_rows)):
        for col in range(len(trees_columns)):
            
            if col == 0 or r == 0 or \
               col ==  len(trees_rows)-1 or \
               r == len(trees_rows)-1:
                   continue
               
            tree = trees_rows[r][col]
            pattern = re.compile(f'[{tree}-9]')
            
            left = find_distance(pattern, trees_rows[r][:col][::-1])
            right = find_distance(pattern, trees_rows[r][col+1:])
            top = find_distance(pattern, trees_columns[col][:r][::-1])
            bottom = find_distance(pattern, trees_columns[col][r+1:])

            score = left*right*top*bottom
            max_score = max(score, max_score)

    return max_score
    

if __name__ == "__main__":
    find_max_view()
