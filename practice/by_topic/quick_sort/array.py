def partition(array, start, stop):
    pivot = array[stop]

    i = start - 1
    for j in range(start, stop):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    i += 1
    array[i], array[stop] = array[stop], array[i]
    return i

def quick_sort(array, start, stop):
    if(start < stop):
        middle = partition(array, start, stop)
        quick_sort(array, start, middle - 1)
        quick_sort(array, middle + 1, stop)


if __name__ == "__main__":
    array = [7, 14, 3, 1, 10, 8, 2, 5]
    quick_sort(array, 0, len(array) - 1)
    print(array)