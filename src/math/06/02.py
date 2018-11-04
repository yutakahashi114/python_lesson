import matplotlib.pyplot as plt
import random

def transformation_1(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x
    y1 = 0.5 * y
    return x1, y1

def transformation_2(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x + 0.5
    y1 = 0.5 * y + 0.5
    return x1, y1

def transformation_3(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x + 1
    y1 = 0.5 * y
    return x1, y1

def transform(p):
    transformations = [transformation_1, transformation_2, transformation_3]
    t = random.choice(transformations)
    x, y = t(p)
    return x, y

def build_tri(p, n):
    x = [p[0]]
    y = [p[1]]
    for i in range(n):
        p = transform(p)
        x.append(p[0])
        y.append(p[1])
    return x, y

if __name__ == '__main__':
    p = [0, 0]
    n = int(input('Enter number : '))
    x, y = build_tri(p, n)
    plt.plot(x, y, 'o')
    plt.savefig('02.png')
