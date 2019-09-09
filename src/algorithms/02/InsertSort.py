def insert_sort(array):
    length = len(array)
    for j in range(1, length):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key
    return array

array = [5, 2, 4, 6, 1, 3]

print(insert_sort(array))
