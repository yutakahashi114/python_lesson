from sympy import *

# def time_period(length):
#     g = 9.8
#     T = 2 * pi * (length / g)** 0.5
#     return T

# if __name__ == '__main__':
#     L = FiniteSet(15, 18, 21, 22.5, 25)
#     for l in L:
#         t = time_period(l/100)
#         print('Length : {0} cm, Time period : {1:.3f} s'.format(float(l), float(t)))

def time_period(length, g):
    # g = 9.8
    T = 2 * pi * (length / g)** 0.5
    return T

if __name__ == '__main__':
    L = FiniteSet(15, 18, 21, 22.5, 25)
    G = FiniteSet(9.8, 9.78, 9.83)
    print('{0:^15}{1:^15}{2:^15}'.format('Length(cm)', 'Gravity(m/s^2)', 'Time Period(s)'))
    for elem in L * G:
        l = elem[0]
        g = elem[1]
        t = time_period(l / 100, g)

        print('{0:^15}{1:^15}{2:^15.3f}'.format(float(l), float(g), float(t)))
