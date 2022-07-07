# We're given n soliders, each with a different height and number p <= q <= n
# p and q define indexes in the sorted array
# We're supposet to return an array (not necessarily) that contains all elements from p to q in the sorted array.

# The solution is to find the p-th and q-th values in the sorted array (low, high). This takes O(n) time since the select function is O(n)
# After that we take all the elemets from array that satisfy the condition low <= element <= high

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

def section(array, p, q):
    result = [0 for i in range(q-p+1)]
    low  = select(array, 0, len(array) - 1, p)
    high  = select(array, 0, len(array) - 1, q)
    index = 0
    for elem in array:
        if low <= elem <= high:
            result[index] = elem
            index += 1
    
    return result

