import matplotlib.pyplot as plt

if __name__ == '__main__':

    x_values = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
    y_values = []
    for x in x_values:
        y = x ** 2 + 2 * x + 1
        y_values.append(y)

    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('y = x^2 + 2x + 1')
    plt.savefig('02.png')
