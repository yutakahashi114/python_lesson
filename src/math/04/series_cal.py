from sympy import *

def print_series(n, x_value):
    init_printing(order='rev-lex')
    x = Symbol('x')
    series = x
    for i in range(2, n + 1):
        series = series + (x ** i) / i
    pprint(series)
    series_value = series.subs({x: x_value})
    print('Value of the series at {0} : {1}'.format(x_value, series_value))

if __name__ == '__main__':
    n = input('Enter the number : ')
    x_value = input('Enter x : ')
    print_series(int(n), float(x_value))
