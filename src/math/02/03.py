import matplotlib.pyplot as plt
import math

def frange(start, final, increment):
    numbers = []
    while start < final:
        numbers.append(start)
        start += increment
    return numbers

def draw_trajectory(u, theta):
    theta_r = math.radians(theta)
    g = 9.8
    t_flight = 2 * u * math.sin(theta_r) / g
    intervals = frange(0, t_flight, 0.001)
    x_max = 0
    y_max = 0
    x = []
    y = []
    for t in intervals:
        x_value = u * math.cos(theta_r) * t
        y_value = u * math.sin(theta_r) * t - 0.5 * g * t * t
        if x_max < x_value:
            x_max = x_value
        if y_max < y_value:
            y_max = y_value
        x.append(x_value)
        y.append(y_value)
    plt.plot(x, y)
    print('velocity = {0}, angle = {1} : flight time = {2}, max horizontal distance = {3}, max vertical distance = {4}'.format(u, theta, t_flight, x_max, y_max))
    
if __name__ == '__main__':

    try:
        count = int(input('How many trajectories? : '))
    except ValueError:
        print('invalid input')
    else:
        u_list = []
        theta_list = []
        for i in range(count):
            try:
                u = float(input('Initial velocity (m/s) : '))
                theta = float(input('angle (degrees) : '))
            except ValueError:
                print('invalid input')
            else:
                u_list.append(u)
                theta_list.append(theta)
                # draw_trajectory(u, theta)

        length = len(u_list)
        legend = []
        for j in range(length):
            u = u_list[j]
            theta = theta_list[j]
            legend.append('u : {0}, theta : {1}'.format(u, theta))
            draw_trajectory(u, theta)
            
        plt.legend(legend)
        plt.xlabel('x-coordinate')
        plt.ylabel('y-coordinate')
        plt.title('Projectile motion of a ball')

        plt.savefig('03.png')
