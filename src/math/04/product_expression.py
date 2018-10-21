from sympy import Symbol, expand, sympify, pprint
from sympy.core.sympify import SympifyError

def product_my(expr1, expr2):
    prod = expand(expr1 * expr2)
    pprint(prod)

if __name__ == '__main__':
    x = Symbol('x')
    y = Symbol('y')
    expr1 = input('Enter : ')
    expr2 = input('Enter : ')

    try:
        expr1 = sympify(expr1)
        expr2 = sympify(expr2)
    except SympifyError:
        print('Invalid input')
    else:
        product_my(expr1, expr2)
