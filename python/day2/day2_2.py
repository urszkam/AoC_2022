from day2_1 import _get_input


def count_score():
    rounds = _get_input()
    total = 0
    win = 6; draw = 3; rock = 1; paper = 2; scissors = 3
    scores = {'A X': scissors, 'A Y': draw+rock, 'A Z': win+paper,
              'B X': rock, 'B Y': draw+paper, 'B Z': win+scissors,
              'C X': paper, 'C Y': draw+scissors, 'C Z': win+rock}
    for round in rounds:
        total += scores[round[:-1]]
        
    return total
