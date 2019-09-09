def merge_sort(array):
    length = len(array)
    if length == 1:
        return array
    half_length = int(length / 2)
    f = []
    b = []
    for i in range(0, half_length):
        f.append(array[i])
    for i in range(half_length, length):
        b.append(array[i])
    f = merge_sort(f)
    b = merge_sort(b)
    f.append(float('inf'))
    b.append(float('inf'))
    merged_array = []
    i = 0
    j = 0
    while i < half_length or j < (length - half_length):
        if f[i] < b[j]:
            merged_array.append(f[i])
            i += 1
        else:
            merged_array.append(b[j])
            j += 1
    return merged_array

array = [5, 2, 4, 6, 1, 3]

print(merge_sort(array))
