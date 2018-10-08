from fractions import Fraction

def add(a, b):
    print('Result od add : {0}'.format(a + b))
def sub(a, b):
    print('Result od sub : {0}'.format(a - b))
def mul(a, b):
    print('Result od mul : {0}'.format(a * b))
def div(a, b):
    print('Result od div : {0}'.format(a / b))
    
if __name__ == '__main__':
    try:
        a = Fraction(input('First friction : '))
        b = Fraction(input('Second friction : '))
        op = input('Operation (Add, Sub, Mul, Div) : ')
        if op == 'Add':
            add(a, b)
        elif op == 'Sub':
            sub(a, b)
        elif op == 'Mul':
            mul(a, b)
        elif op == 'Div':
            div(a, b)
    except ValueError:
        print('Invalid number')
