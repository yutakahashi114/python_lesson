import math
from sympy import *

def grad_ascent(x0, f1x, x):
    if not solve(f1x):
        print('Cannot solve {0}=0'.format(f1x))
        return
    epsilon = 1e-6
    step_size = 1e-4
    x_old = x0
    x_new = x_old + step_size * f1x.subs({x: x_old}).evalf()
    while abs(x_old - x_new) > epsilon:
        x_old = x_new
        x_new = x_old + step_size * f1x.subs({x: x_old}).evalf()
    return x_new

if __name__ == '__main__':
    f = input('Enter function : ')
    var = input('Enter variable : ')
    var0 = float(input('Enter initial variable : '))
    try:
        f = sympify(f)
    except SympifyError:
        print('Invalid function')
    else:
        var = Symbol(var)
        d = Derivative(f, var).doit()
        var_max = grad_ascent(var0, d, var)
        if var_max:
            print('{0} : {1}'.format(var.name, var_max))
            print('Maximun value : {0}'.format(f.subs({var: var_max})))
