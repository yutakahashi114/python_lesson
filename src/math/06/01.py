import matplotlib.pyplot as plt

def draw_square():
    ax = plt.axes(xlim=(0, 6), ylim=(0, 6))
    ax.set_aspect('equal')
    square = plt.Polygon([(1, 1), (5, 1), (5, 5), (1, 5)], closed=True)
    ax.add_patch(square)
    y = 1.5
    while y <= 4.5:
        x = 1.5
        while x <= 4.5:
            circle = plt.Circle((x, y), radius=0.5, fc='w')
            ax.add_patch(circle)
            x += 1
        y += 1

    plt.savefig('01.png')

if __name__ == '__main__':
    draw_square()
