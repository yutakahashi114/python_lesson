from sympy import *
from sympy.core.sympify import SympifyError

def search_factor(expr):
    factors = factor(expr)
    pprint(factors)
    
if __name__ == '__main__':
    expr = input('Enter expression : ')
    try:
        expr = sympify(expr)
    except SympifyError:
        print('Invalid input')
    else:
        search_factor(expr)

