from matplotlib_venn import venn2
import matplotlib.pyplot as plt
from sympy import FiniteSet
import csv

def read_csv(filename):
    football = []
    other = []
    with open(filename) as f:
        reader = csv.reader(f)
        # 1行目はヘッダなので、飛ばす
        next(reader)
        for row in reader:
            if int(row[1]) == 1:
                football.append(int(row[0]))
            if int(row[2]) == 1:
                other.append(int(row[0]))
    return football, other

def draw_venn(sets):
    venn2(subsets=sets, set_labels=('Football', 'Other'))
    plt.savefig('01.png')

if __name__ == '__main__':
    # s1 = FiniteSet(1, 3, 5, 7, 9, 11, 13, 15, 17, 19)
    # s2 = FiniteSet(2, 3, 5, 7, 11, 13, 17, 19)
    # draw_venn([s1, s2])
    football, other = read_csv('../file/sports.csv')
    footballSet = FiniteSet(*football)
    otherSet = FiniteSet(*other)
    draw_venn([footballSet, otherSet])
