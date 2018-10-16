from collections import Counter
def frequency_table(numbers):
    table = Counter(numbers)
    numbers_freq = table.most_common()
    numbers_freq.sort()
    print('Number\tFrequency')
    for number in numbers_freq:
        print('{0}\t{1}'.format(number[0], number[1]))

if __name__ == '__main__':
    scores = [7, 8, 9, 2, 6, 6, 6, 8, 8, 6, 3, 9, 10, 1, 3, 7, 5, 7, 8, 5, 7]
    frequency_table(scores)
