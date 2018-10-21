from sympy import *

def print_series(n):
    init_printing(order='rev-lex')
    x = Symbol('x')
    series = x
    for i in range(2, n + 1):
        series = series + (x ** i) / i
    pprint(series)    
        
if __name__ == '__main__':
    n = input('Enter the number : ')
    print_series(int(n))
