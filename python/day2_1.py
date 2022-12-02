def _get_input():
    with open('./input/day2.txt', 'r') as data:
        return (x for x in data.readlines())
    
    
def count_score():
    rounds = _get_input()
    total = 0
    scores = {'A X': 4, 'A Y': 8, 'A Z': 3,
              'B X': 1, 'B Y': 5, 'B Z': 9,
              'C X': 7, 'C Y': 2, 'C Z': 6}
    for round in rounds:
        total += scores[round[:-1]]
        
    return total
    