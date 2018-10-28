from sympy import *
from fractions import Fraction
import random

# s = FiniteSet(1, 2, 3, 1.5, Fraction(1, 5))
# print(len(s))
# print(s)

# print(4 in s)
# print(5 in s)

# print(FiniteSet())

# members = [1, 2, 3, 2]
# t = FiniteSet(*members)
# print(t)

# for member in t:
#     print(member)

# u = FiniteSet(3, 2, 1)
# print(t == u)

# print(s.is_subset(t))
# print(t.is_subset(s))

# print(s.is_superset(t))
# print(t.is_superset(s))

# print(t.powerset())
# print(len(t.powerset()))

# print(u.is_proper_superset(t))
# print(t.is_proper_superset(u))

# print(s.is_proper_superset(t))
# print(t.is_proper_superset(s))

# v = FiniteSet(1, 2, 3)
# w = FiniteSet(2, 4, 6)
# x = FiniteSet(3, 5, 7)
# print(v.union(w))
# print(v.intersect(w))

# print(v.union(w).union(x))
# print(v.intersect(w).intersect(x))

# p = v * w
# for elem in p:
#     print(elem)

# print(len(p) == len(v) * len(w))

# for elem in v ** 2:
#     print(elem)

s = FiniteSet(1, 2, 3, 4, 5, 6)
a = FiniteSet(2, 3, 5)
b = FiniteSet(1, 3, 5)
e = a.union(b)
print(len(e) / len(s))

f = a.intersect(b)
print(len(f) / len(s))

print(random.randint(1, 6))
