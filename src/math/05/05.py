from sympy import *
import random

def is_inner_circle(radius, x, y):
    result = (x ** 2 + y ** 2 < radius ** 2)
    return result

if __name__ == '__main__':
    radius = float(input('Radius : '))
    counts = FiniteSet(1000, 100000, 1000000)
    area = float(pi * (radius ** 2))
    for count in counts:
        inner_count = 0
        for index in range(0, count):
            x = random.uniform(-radius, radius)
            y = random.uniform(-radius, radius)
            if is_inner_circle(radius, x, y):
                inner_count += 1
        f = inner_count / int(count)
        estimated_area = f * ((2 * radius)** 2)
        estimated_pi = f * 4
        print('Area : {0}, count : {1}, Estimated : {2}, Pi : {3}'.format(area, count, estimated_area, estimated_pi))
