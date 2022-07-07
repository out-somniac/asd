# Quick sort algorithm. Average time complexity Θ(nlog(n)). 
# Worst case scenario time complexity O(n^2).
# This algorithm uses a hoare partition scheme

def partition(array, start, stop):
    """ 
    Hoare partition scheme. 
    Divides an array in two so that all numbers lesser than the pivot are to the left
    and all greater are right to the pivot. 
    """

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
    """ Recursively sorts left and right side of the array """
    if(start < stop):
        middle = partition(array, start, stop)
        quick_sort(array, start, middle - 1)
        quick_sort(array, middle + 1, stop)