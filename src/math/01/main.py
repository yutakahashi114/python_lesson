from fractions import Fraction
# f = Fraction(3, 4)
# f += 1.5
# print(f)

# a = 4 + 3j
# b = 2 - 3j
# print (abs(a))
# print (a/b)

# c = int(input())
# print (type(c))

# try:
#     a = float(input('Enter a number: '))
#     print (a)
# except ValueError:
#     print('You entered an invalid number')

# try:
#     a = Fraction(input('Enter a number: '))
#     print (a)
# except ValueError:
#     print('You entered an invalid number')

# try:
#     a = complex(input('Enter a number: '))
#     print (a)
# except ValueError:
#     print('You entered an invalid number')

def isFactor(a, b):
    if b % a == 0:
        return True
    else:
        return False

# print(isFactor(4, 1024))

# for i in range(1, 10, 3):
#     print(i)

# item1 = 'a'
# item2 = 'b'
# item3 = 'c'
# print('item_1: {0} item_2: {1} item_3: {2}'.format(item1, item2, item3))

