import read_file

def calculate_percentile(numbers, p):
    numbers.sort()
    n = len(numbers)
    i = n * p / 100 + 0.5
    if i.is_integer():
        return numbers[int(i - 1)]
    k = int(i / 1)
    f = i - k
    return (1 - f) * numbers[k - 1] + f * numbers[k]
    
if __name__ == '__main__':
    data = read_file.read_data('test.txt')
    try:
        p = float(input('Enter percentile : '))
        print(calculate_percentile(data, p))
    except ValueError:
        print('Invalid number')
    