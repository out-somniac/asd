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