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

def select(array, start, stop, k):
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