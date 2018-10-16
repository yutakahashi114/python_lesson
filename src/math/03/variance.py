def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s / N
    return mean

def find_differences(numbers):
    mean = calculate_mean(numbers)
    diff = []
    for number in numbers:
        diff.append(number - mean)
    return diff

def calculate_variance(numbers):
    diff = find_differences(numbers)
    squared_diff = []
    for d in diff:
        squared_diff.append(d ** 2)
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff / len(numbers)
    return variance

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    variance = calculate_variance(donations)
    print('Variance : ' + str(variance))
    print('Standard deviation : ' + str(variance ** 0.5))
