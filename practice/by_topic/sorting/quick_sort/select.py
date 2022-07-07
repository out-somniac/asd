# Basic quick-select algorithm that finds the k-th smallest element in in an unsorted array.
# It's time complexity is Θ(n). Worst case O(n^2)
# Some similar algorithms: 
#   - Floyd-Rivest algorithm
#   - Partial sorting using a heap
#   - Median of medians

def partition(array, start, stop):
    """ Function that uses a hoare partition scheme to divide the array in two """
    pivot = array[stop]
    i = start - 1
    for j in range(start, stop):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    i += 1
    array[i], array[stop] = array[stop], array[i]
    return i

def select(array, start, stop, k):
    """ Main algorithm implementation. Divides the array in two parts and recur for one part of this array. """
    if stop == start:
        return array[start]
    if start < stop:
        q = partition(array, start, stop)
        if q == k:
            return array[q]
        elif q < k:
            return select(array, q + 1, stop, k)
        else:
            return select(array, start, q - 1, k)