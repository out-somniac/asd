def partition(array, start, stop):
    pivot = array[stop]

    i = start
    for j in range(start, stop):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i - 1]
            i += 1
    i += 1
    array[i - 1], array[stop] = array[stop], array[i - 1]
    return i - 1

def quick_sort(array, start, stop):
    if(start < stop):
        middle = partition(array, start, stop)
        quick_sort(array, start, middle - 1)
        quick_sort(array, middle + 1, stop)


if __name__ == "__main__":
    array = [7, 14, 3, 1, 10, 8, 2, 5]
    quick_sort(array, 0, len(array) - 1)
    print(array)