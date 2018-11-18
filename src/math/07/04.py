from sympy import *

if __name__ == '__main__':
    f = input('Enter function : ')
    var = input('Enter valiable : ')
    var_min = float(input('Enter min : '))
    var_max = float(input('Enter max : '))

    try:
        f = sympify(f)
    except SympifyError:
        print('Invalid function')
    else:
        var = Symbol(var)
        d = Derivative(f, var)
        g = (1+d**2)**0.5
        result = Integral(g, (var, var_min, var_max)).doit().evalf()
        print('Length : {0}'.format(result))
