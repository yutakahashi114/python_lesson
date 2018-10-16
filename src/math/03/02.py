import mean
import median
import mode
import variance
import read_file

if __name__ == '__main__':
    data = read_file.read_data('test.txt')

    # 平均
    mean = mean.calculate_mean(data)
    print('Mean : ' + str(mean))
    # 中央値
    median = median.calculate_median(data)
    print('Median : ' + str(median))
    # 最頻値
    modes = mode.calculate_mode(data)
    print('Mode :')
    for mode in modes:
        print('\t' + str(mode))
    # 分散
    variance = variance.calculate_variance(data)
    print('Variance : ' + str(variance))
    # 標準偏差
    print('Standard deviation : ' + str(variance ** 0.5))
