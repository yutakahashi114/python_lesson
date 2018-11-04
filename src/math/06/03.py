import matplotlib.pyplot as plt
from matplotlib import animation

def transformation(p):
    x = p[0]
    y = p[1]
    x1 = y + 1 - 1.4 * x * x
    y1 = 0.3 * x
    return x1, y1

def build_henon(p, n):
    x = [p[0]]
    y = [p[1]]
    for i in range(n):
        p = transformation(p)
        x.append(p[0])
        y.append(p[1])
    return x, y

def update_position(i, circle, x, y):
    circle.center = x[i], y[i]
    return circle,

def create_animation(p, n):
    x, y = build_henon(p, n)

    fig = plt.gcf()
    ax = plt.axes(xlim=(-1.5, 1.5), ylim=(-1.5, 1.5))
    # ax.set_aspect('equal')

    circle=plt.Circle(p, 0.05)
    ax.add_patch(circle)
    anim=animation.FuncAnimation(
        fig,
        update_position,
        fargs=(circle, x, y),
        frames=n,
        repeat = False
    )
    plt.title('Projectile Motion')
    plt.xlabel('X')
    plt.ylabel('Y')
    anim.save('03.gif', writer="imagemagick")

if __name__ == '__main__':
    p = (1, 1)
    n = int(input('Enter number : '))
    create_animation(p, n)
