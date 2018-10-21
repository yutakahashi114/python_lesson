from sympy import *
from sympy.core.sympify import SympifyError

def calculate_sum(expr, n_max):
    n = Symbol('n')
    sum = summation(expr, (n, 1, n_max))
    return sum
    
if __name__ == '__main__':
    expr = input('Enter expression : ')
    n_max = input('Number : ')
    try:
        expr = sympify(expr)
        n_max = int(n_max)
    except SympifyError:
        print('Invalid input')
    else:
        sum = calculate_sum(expr, n_max)
        pprint(sum)
