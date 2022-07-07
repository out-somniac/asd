def count_sort(array, place_exp):
    n = len(array)
    counts = [0 for i in range(10)]
    output = [0 for i in range(n)]

    for elem in array:
        index = (elem // place_exp) % 10
        counts[index] += 1
    for i in range(1, 10):
        counts[i] = counts[i] + counts[i - 1]

    i = n - 1
    while i >= 0:
        index = (array[i] // place_exp) % 10
        output[counts[index] - 1] = array[i]
        counts[index] -= 1
        i -= 1
    
    for i in range(n):
        array[i] = output[i]

def radix_sort(array):
    max_number = max(array)

    place_exp = 1
    while max_number > place_exp:
        count_sort(array, place_exp)
        place_exp *= 10

array = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(array)
print(array)