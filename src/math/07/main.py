import math
from sympy import *

theta = Symbol('theta')
# print(math.sin(theta) + math.sin(theta))
# print(sin(theta) + sin(theta))

# x = Symbol('x', positive=True)
# if (x + 5) > 0:
#     print('a')
# else:
#     print('b')

x = Symbol('x')
n = Symbol('n')
# l = Limit(1/x, x, S.Infinity)
# print(l)
# print(l.doit())
# print(Limit(1/x, x, 0, dir='-').doit())
# print(Limit(1/x, x, 0, dir='+').doit())
# print(Limit(sin(x)/x, x, 0).doit())
# print(Limit((1 + 1/n)**n, n, S.Infinity).doit())

p = Symbol('p', positive=True)
r = Symbol('r', positive=True)
t = Symbol('t', positive=True)

# print(Limit(p * (1 + r / n)**(n * t), n, S.Infinity).doit())

# St = 5 * t * t + 2 * t + 8
# t1 = Symbol('t1')
# delta_t = Symbol('delta_t')

# St1 = St.subs({t: t1})
# St_delta = St.subs({t: t1 + delta_t})

# print(Limit((St_delta - St1)/delta_t, delta_t, 0).doit())
# d = Derivative(St, t)
# print(d.doit())
# print(d.doit().subs({t: t1}))
# print(d.doit().subs({t: 1}))

# f = (x ** 3 + x ** 2 + x) * (x ** 2 + x)
# d = Derivative(f, x)
# print(d.doit())
# print(d.doit().expand())

# f = x ** 5 - 30 * x ** 3 + 50 * x
# d1 = Derivative(f, x).doit()
# critical_points = solve(d1)
# pprint(critical_points)

# A = critical_points[2]
# B = critical_points[0]
# C = critical_points[1]
# D = critical_points[3]

# d2 = Derivative(f, x, 2).doit()

# print(d2.subs({x:B}).evalf())
# print(d2.subs({x:C}).evalf())
# print(d2.subs({x:A}).evalf())
# print(d2.subs({x:D}).evalf())

# x_min = -5
# x_max = 5

# print(f.subs({x:C}).evalf())
# print(f.subs({x:A}).evalf())
# print(f.subs({x:x_min}).evalf())
# print(f.subs({x:x_max}).evalf())

print(Integral(n*x, x).doit())
print(Integral(n*x, (x, 0, 2)).doit())

p = exp(-(x - 10)** 2 / 2) / sqrt(2 * pi)
print(Integral(p, (x, 11, 12)).doit())
# print(Integral(p, (x, 11, 12)).doit().evalf())
print(Integral(p, (x, S.NegativeInfinity, S.Infinity)).doit().evalf())
