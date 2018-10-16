import matplotlib.pyplot as plt
import math

def frange(start, final, increment):
    numbers = []
    while start < final:
        numbers.append(start)
        start += increment
    return numbers

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')
    
def draw_trajectory(u, theta):
    theta = math.radians(theta)
    g = 9.8
    t_fright = 2 * u * math.sin(theta) / g
    intervals = frange(0, t_fright, 0.001)
    x = []
    y = []
    for t in intervals:
        x.append(u * math.cos(theta) * t)
        y.append(u * math.sin(theta) * t - 0.5 * g * t * t)
    draw_graph(x, y)
    
if __name__ == '__main__':
    # try:
    #     u = float(input('Initial velocity (m/s) : '))
    #     theta = float(input('angle (degrees) : '))
    # except ValueError:
    #     print('invalid input')
    # else:
    #     draw_trajectory(u, theta)

    u_list = [20, 40, 60]
    theta = 45
    for u in u_list:
        draw_trajectory(u, theta)
        
    plt.legend(['20', '40', '60'])
    plt.savefig('projectile_motion.png')
