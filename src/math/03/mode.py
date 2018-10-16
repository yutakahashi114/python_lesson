from collections import Counter

def calculate_mode(numbers):
    c = Counter(numbers)
    numbers_freq = c.most_common()
    max_count = numbers_freq[0][1]
    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            modes.append(num[0])
    return modes

if __name__ == '__main__':
    scores = [7, 8, 9, 2, 6, 6, 6, 8, 8, 6, 3, 9, 10, 1, 3, 7, 5, 7, 8, 5, 7]
    modes = calculate_mode(scores)
    print('Mode of score is :')
    for mode in modes:
        print(mode)
