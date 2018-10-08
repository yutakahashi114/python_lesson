def is_even():
    n = input('Enter a number : ')
    if n.isdigit():
        n = int(n)
        if n % 2 == 0:
            print('even')
            print_number(n)
        else:
            print('odd')
            print_number(n)
    else:
        print('Please enter integer')

def print_number(n):
    for i in range(1, 10):
        print(n + i * 2)

if __name__ == '__main__':
    is_even()
