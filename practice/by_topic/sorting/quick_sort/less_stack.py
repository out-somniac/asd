# Quick sort algorithm that uses only O(log(n)) stack frames in the worst case scenario
# This approach uses tail recursion optimisation
# Worst case time complexity O(n^2)
# Average case time complexity Θ(nlog(n))

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
    while start < stop:
        pi = partition(array, start, stop)
        
        if pi - start < stop - pi:
            quick_sort(array, start, pi - 1)
            start = pi + 1
        else:
            quick_sort(array, pi + 1, stop)
            stop = pi - 1