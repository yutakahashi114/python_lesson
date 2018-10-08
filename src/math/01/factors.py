'''
Find the factor of an integer
'''

def factors(b):
    for i in range(1, b + 1):
        if b % i == 0:
            print(i)

if __name__ == '__main__':
    b = input('Your number please : ')
    if b.isdigit():
        b = int(b)
        if b > 0:
            factors(b)
        else:
            print('Please enter a positive integer')
    else:
        print('Please enter a positive integer')
