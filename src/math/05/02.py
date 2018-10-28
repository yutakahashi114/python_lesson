from sympy import FiniteSet
import random

if __name__ == '__main__':
    counts = FiniteSet(100, 1000, 10000, 100000, 500000)
    print('Expected value: 3.5')
    for count in counts:
        sum = 0
        for index in range(1, count + 1):
            number = random.randint(1, 6)
            sum += number
        average = sum / int(count)
        print('Trials : {0}, Average : {1}'.format(count, average))
