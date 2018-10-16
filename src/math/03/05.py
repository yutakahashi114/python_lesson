import read_file

def create_classes(numbers, n):
    low = min(numbers)
    high = max(numbers)
    width = (high - low) / n
    classes = []
    a = low
    b = low + width
    while b < high:
        classes.append((a, b))
        a = b
        b += width
    classes.append((a, high + 1))

    return classes
    
def calculate_classes_count(classes, numbers):
    counts = [0] * len(classes)

    for number in numbers:
        for i, class_range in enumerate(classes):
            if (class_range[0] <= number and number < class_range[1]):
                counts[i] += 1
                break

    return counts

def create_table(classes, counts):
    print('\tclasses\t\tcount')
    for i, class_range in enumerate(classes):
        print(str(class_range[0]) + '\t-\t' + str(class_range[1]) + '\t' + str(counts[i]))
        

if __name__ == '__main__':
    data = read_file.read_data('test.txt')
    try:
        n = float(input('Enter class size : '))
        classes = create_classes(data, n)
        counts = calculate_classes_count(classes, data)
        create_table(classes, counts)
    except ValueError:
        print('Invalid number')
    