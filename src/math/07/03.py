from sympy import *

if __name__ == '__main__':
    f = input('Enter f : ')
    g = input('Enter g : ')
    var = input('Enter valiable : ')

    try:
        f = sympify(f)
        g = sympify(g)
    except SympifyError:
        print('Invalid function')
    else:
        var = Symbol(var)
        h = f - g
        s = solve(h)
        if not s:
            print('Do not intersect')
        elif len(s) != 2:
            print('Can not calculate')
        elif h.subs({var: (s[0] + s[1])/2}).evalf() < 0:
            print('f is not Upper function')
        else:
            result = Integral(h, (var, s[0], s[1])).doit().evalf()
            print('Area : {0}'.format(result))
