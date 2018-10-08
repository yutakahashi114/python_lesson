def multi_table(a, n):
    for i in range(1, n + 1):
        print('{0:.0f} * {1} = {2:.0f}'.format(a, i, a * i))

if __name__ == '__main__':
    while True:
        a = input('Enter a number1 : ')
        n = input('Enter a number2 : ')
        multi_table(float(a), int(n))
        answer = input('exit? (y) for yes ')
        if answer == 'y':
            break
