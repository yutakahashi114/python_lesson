def multi_table(a):
    for i in range(1, 11):
        print('{0:.0f} * {1} = {2:.0f}'.format(a, i, a * i))

if __name__ == '__main__':
    a = input('Enter a number : ')
    multi_table(float(a))
