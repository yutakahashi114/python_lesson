# from pylab import plot, show
import matplotlib.pyplot as plot

simplelist = [1, 3, 5]
print(simplelist[0])
print(simplelist[1])
print(simplelist[2])

simplelist[2] = 7
print(simplelist[2])

emptylist = []
emptylist.append(1)
emptylist.append(4)
emptylist.append(6)
print(emptylist)

simplelist = (1, 3, 5)
print(simplelist)
print(simplelist[2])
print(simplelist[-1])

for index, value in enumerate(simplelist):
    print('{0} => {1}'.format(index, value))

x_numbers = [1, 2, 3]
y_numbers = [2, 4, 6]

plot.plot(x_numbers, y_numbers)
plot.savefig('main.png')
