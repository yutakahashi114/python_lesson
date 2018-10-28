import random

def toss():

    return random.randint(1, 6)

if __name__ == '__main__':
    money = int(input('Enter your money : '))
    count = 0
    while money > 0:
        toss = random.randint(1, 2)
        if toss == 1:
            money += 1
        else:
            money -= 1.5
        print('Current money : {0}'.format(money))
        count += 1
    print('Game Over : (money : {0}, tosses : {1})'.format(money, count))
