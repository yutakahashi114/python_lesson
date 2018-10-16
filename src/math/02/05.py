import matplotlib.pyplot as plt

def fibo(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    
    a = 1
    b = 1
    series = [1, 1]
    for i in range(n - 2):
        c = a + b
        series.append(c)
        a = b
        b = c
    return series

if __name__ == '__main__':
    number = 100
    fibo = fibo(number)
    ratio_list = []
    # no_list = []
    no_list = range(number - 1)
    for i in range(number - 1):
        ratio_list.append(fibo[i + 1] / fibo[i])
        # no_list.append(i)

    plt.plot(no_list, ratio_list)
    plt.xlabel('No.')
    plt.ylabel('Ratio')
    plt.title('Fibo Ratio')

    plt.savefig('05.png')
    