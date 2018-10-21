from sympy import *
from sympy.plotting import plot
from sympy.core.sympify import SympifyError

def plot_expression(expr):
    x, y, z, a, b, c, s, t, u = symbols('x,y,z,a,b,c,s,t,u')
    solution = solve(expr, y)
    expr_y = solution[0]
    p = plot(expr_y, (x, -5, 5), title='A Line', xlabel='x', ylabel='y', show=False)
    p.save('plot_graph.png')
    
if __name__ == '__main__':
    expr = input('Enter expression : ')
    try:
        expr = sympify(expr)
    except SympifyError:
        print('Invalid input')
    else:
        plot_expression(expr)

