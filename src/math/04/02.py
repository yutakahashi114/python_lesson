from sympy import *
from sympy.core.sympify import SympifyError

def plot_graphs(expr1, expr2):
    y = Symbol('y')
    solve1 = solve(expr1, y)
    sol1 = solve1[0]
    solve2 = solve(expr2, y)
    sol2 = solve2[0]
    p = plot(sol1, sol2, legend=True, show=False)
    p[0].line_color = 'b'
    p[1].line_color = 'r'
    p.save('02.png')
    
if __name__ == '__main__':
    expr1 = input('Enter expression1 : ')
    expr2 = input('Enter expression2 : ')
    try:
        expr1 = sympify(expr1)
        expr2 = sympify(expr2)
    except SympifyError:
        print('Invalid input')
    else:
        plot_graphs(expr1, expr2)
        solve = solve((expr1, expr2), dict=True)
        soln = solve[0]
        pprint(soln)
