import matplotlib.pyplot as plt

def create_bar_chart(data, labels):
    num_bars = len(data)
    positions = range(1, num_bars + 1)
    plt.barh(positions, data, align='center')
    plt.yticks(positions, labels)
    plt.xlabel('Amount')
    plt.ylabel('Categories')
    plt.title('Weekly expenditures')
    plt.grid()
    plt.savefig('04.png')

if __name__ == '__main__':

    try:
        count = int(input('Enter the number of categories : '))
    except ValueError:
        print('invalid input')
    else:
        category_list = []
        amount_list = []
        for i in range(count):
            try:
                category = input('Enter category : ')
                amount = int(input('Expenditure : '))
            except ValueError:
                print('invalid input')
            else:
                category_list.append(category)
                amount_list.append(amount)
        create_bar_chart(amount_list, category_list)
        