import math
from sympy import *

def limit_p(f, var, x0):
    return Limit(f, var, x0, dir='+').doit()

def limit_m(f, var, x0):
    return Limit(f, var, x0, dir='-').doit()

if __name__ == '__main__':
    f = input('Enter function : ')
    var = input('Enter variable : ')
    x0 = float(input('Enter point : '))
    try:
        f = sympify(f)
    except SympifyError:
        print('invalid function')
    else:
        limit_p = limit_p(f, var, x0)
        limit_m = limit_m(f, var, x0)
        fx0 = f.subs({var: x0}).evalf()
        if limit_m == limit_p == fx0:
            print('{0} is continuous at {1}'.format(f, x0))
        else:
            print('{0} is not continuous at {1}'.format(f, x0))
