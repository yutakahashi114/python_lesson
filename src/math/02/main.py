import matplotlib.pyplot as plt

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

# plt.plot(x_numbers, y_numbers, 'o')

nyc_temp = [53.9, 56.3, 56.4, 53.4]
years = range(2000, 2004)
plt.plot(years, nyc_temp, marker='o')
plt.axis([1999, 2004, 0, 60])

# nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5]
# nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1]
# nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1]
# months = range(1, 6)
# plt.plot(months, nyc_temp_2000)
# plt.plot(months, nyc_temp_2006)
# plt.plot(months, nyc_temp_2012)
# plt.legend([2000, 2006, 2012])
# plt.title('Average monthly temperature in NYC')
# plt.xlabel('Month')
# plt.ylabel('Temperature')
plt.savefig('main.png')
