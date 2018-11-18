def read_data(path):
    numbers = []
    try:
        with open(path) as f:
            lines = f.readlines()
            for line in lines:
                try:
                    n = float(line)
                except ValueError:
                    print('Bad data : {0}'.format(line))
                    # break
                    # return
                    continue
                numbers.append(n)
    except FileNotFoundError:
        print('File not found')
    return numbers

if __name__ == '__main__':
    data_file = input('Enter file name : ')
    data = read_data(data_file)
    print(data)
