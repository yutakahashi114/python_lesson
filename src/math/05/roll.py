# import matplotlib.pyplot as plt
import random

target_score = 20

def roll():
    return random.randint(1, 6)

if __name__ == '__main__':
    score = 0
    number_rolls = 0
    while score < target_score:
        die_roll = roll()
        number_rolls += 1
        print('Rolled : {0}'.format(die_roll))
        score += die_roll

    print('Score : {0}, Rolls : {1}'.format(score, number_rolls))
