import csv
import matplotlib.pyplot as plt
import corr

def scatter_plot(x, y):
    plt.scatter(x, y)
    plt.xlabel('Number')
    plt.ylabel('Square')
    plt.savefig('read_csv_google.png')

def read_csv(filename):
    summer = []
    highest_correlated = []
    with open(filename) as f:
        reader = csv.reader(f)
        # 1行目はヘッダなので、飛ばす
        next(reader)
        for row in reader:
            summer.append(float(row[1]))
            highest_correlated.append(float(row[2]))
    return summer, highest_correlated

if __name__ == '__main__':
    summer, highest_correlated = read_csv('../file/correlate-summer.csv')
    correlate = corr.find_corr_x_y(summer, highest_correlated)
    print('Correlation : ' + str(correlate))
    scatter_plot(summer, highest_correlated)
