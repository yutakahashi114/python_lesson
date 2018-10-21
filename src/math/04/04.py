from sympy import *
from sympy.core.sympify import SympifyError

if __name__ == '__main__':
    expr = input('Enter expression : ')
    ineq_obj = sympify(expr)
    lhs = ineq_obj.lhs
    x = Symbol('x')

    if lhs.is_polynomial():
        p = Poly(lhs, x)
        rel = ineq_obj.rel_op
        pprint(solve_poly_inequality(p, rel))
    elif lhs.is_rational_function():
        numer, denom = lhs.as_numer_denom()
        p1 = Poly(numer)
        p2 = Poly(denom)
        rel = ineq_obj.rel_op
        pprint(solve_rational_inequalities([[((p1, p2), rel)]]))
    else:
        pprint(solve_univariate_inequality(ineq_obj, x, relational=False))
