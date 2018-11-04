import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random

def initialize_image(x_p, y_p):
    image = []
    for i in range(y_p):
        x_colors = []
        for j in range(x_p):
            x_colors.append(0)
        image.append(x_colors)
    return image

def color_points():
    x_p = 400
    y_p = 400
    image = initialize_image(x_p, y_p)

    x_min = -2.5
    x_max = 1.0
    y_min = -1.0
    y_max = 1.0

    max_iteration = 1000

    yk = y_min
    for i in range(y_p):
        xi = x_min
        for k in range(x_p):
            z1 = 0
            c = complex(xi, yk)
            iteration = 0
            while True:
                z1 = z1 * z1 + c
                iteration += 1
                if not(abs(z1) < 2 and iteration < max_iteration):
                    break
            image[i][k] = iteration
            xi += (x_max - x_min) / x_p
        yk += (y_max - y_min) / y_p

    plt.imshow(
        image,
        origin='lower',
        extent=(x_min, x_max, y_min, y_max),
        cmap=cm.Greys_r,
        interpolation='nearest'
    )
    plt.colorbar()
    plt.savefig('04.png')

if __name__ == '__main__':
    color_points()
