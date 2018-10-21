from sympy import *
from sympy.core.sympify import SympifyError
from sympy.plotting import plot

x = Symbol('x')
# print(x + x + 1)

y, z = symbols('y,z')
f = x * (x + y)
# print(f)

expr = x ** 2 - y ** 2
factors = factor(expr)
# print(factors)
# print(expand(factors))

expr = x ** 3 + 3 * x ** 2 * y + 3 * x * y ** 2 + y ** 3

factors = factor(expr)
# print(factors)
# print(expand(factors))

expr = x + y + x * y
factors = factor(expr)
# print(factors)

expr = x ** 2 + 2 * x * y + y ** 2 + x + y
factors = factor(expr)
# pprint(expr)
# pprint(factors)

expr = 1 + 2 * x + 2*x**2
# pprint(expr)
init_printing()
# init_printing(order='rev-lex')
# pprint(expr)

expr = x ** 2 + 2 * x * y + y ** 2
res = expr.subs({x: 1, y: 2})
print(res)

expr = x ** 2 + 2 * x * y + y ** 2
res = expr.subs({x: 1 - y})
print(simplify(res))

# text = input('Enter : ')
# try:
#     expr = sympify(text)
#     pprint(expr)
#     pprint(2*expr)
# except SympifyError:
#     print('invalid input')

# expr = x - 7 - 5
# solve = solve(expr)
# print(solve)

# expr = x**2 + 5*x + 4
# expr = x**2 + x + 1
# solve = solve(expr, dict=True)
# pprint(solve)

a, b, c, s, t, u = symbols('a,b,c,s,t,u')

# expr = a * x * x + b * x + c
# solve = solve(expr, x, dict=True)
# pprint(solve)

expr = u * t + 0.5 * a * t * t - s

t_expr = solve(expr, t, dict=True)
# pprint(t_expr)

expr1 = 2 * x + 3 * y - 6
expr2 = 3 * x + 2 * y - 12
solve = solve((expr1, expr2), dict=True)
# pprint(solve)
soln = solve[0]
# print(expr1.subs({x: soln[x], y: soln[y]}))
# print(expr2.subs({x: soln[x], y: soln[y]}))

p = plot(2 * x + 3, (x, -5, 5), title='A Line', xlabel='x', ylabel='2x+3', show=False)

p = plot(2 * x + 3, 3 * x + 1, legend=True, show=False)
p[0].line_color = 'b'
p[1].line_color = 'r'

p.save('main.png')

# ineq_obj = -x ** 2 + 4 < 0
# lhs = ineq_obj.lhs
# p = Poly(lhs, x)
# rel = ineq_obj.rel_op
# pprint(solve_poly_inequality(p, rel))

# ineq_obj = ((x - 1) / (x + 2)) > 0
# lhs = ineq_obj.lhs
# numer, denom = lhs.as_numer_denom()
# p1 = Poly(numer)
# p2 = Poly(denom)
# rel = ineq_obj.rel_op
# pprint(solve_rational_inequalities([[((p1, p2), rel)]]))

ineq_obj = sin(x) - 0.6 > 0
pprint(solve_univariate_inequality(ineq_obj, x, relational=False))
