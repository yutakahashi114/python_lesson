import math
from sympy import *
import matplotlib.pyplot as plt

def grad_descent(x0, f, x):
    f1x = Derivative(f, x).doit()
    if not solve(f1x):
        print('Cannot solve {0}=0'.format(f1x))
        return
    epsilon = 1e-6
    step_size = 1e-4

    critical_point = solve(f1x)
    c_min = critical_point[0]
    c_max = critical_point[0]
    for c in critical_point:
        if c < c_min:
            c_min = c
        if c > c_max:
            c_max = c
    plot_line(f, c_min, c_max, 0.1, x)

    x_list = []
    y_list = []

    x_old = x0
    x_new = x_old - step_size * f1x.subs({x: x_old}).evalf()
    x_list.append(x_old)
    y_list.append(f.subs({x: x_old}).evalf())
    while abs(x_old - x_new) > epsilon:
        x_old = x_new
        x_new = x_old - step_size * f1x.subs({x: x_old}).evalf()
        x_list.append(x_old)
        y_list.append(f.subs({x: x_old}).evalf())
    plt.plot(x_list, y_list, marker='o')
    return x_new

def plot_line(f, x_min, x_max, step_size, x):
    numbers = []
    start = x_min - 5
    final = x_max + 5
    x_list = []
    y_list = []
    x_list.append(start)
    y_list.append(f.subs({x: start}).evalf())
    while start < final:
        numbers.append(start)
        start += step_size
        x_list.append(start)
        y_list.append(f.subs({x: start}).evalf())
    plt.plot(x_list, y_list)


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
        var_max = grad_descent(var0, f, var)
        if var_max:
            print('{0} : {1}'.format(var.name, var_max))
            print('Mimimun value : {0}'.format(f.subs({var: var_max})))
            plt.savefig('02.png')
