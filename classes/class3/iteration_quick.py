def partition(array, start, stop):
    i = start - 1
    pivot = array[stop]
    for j in range(start, stop):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    i += 1
    array[i], array[stop] = array[stop], array[i]
    return i

# This implements a recursive version of quick_sort
# It works by storing and then poping partition() calls on a stack
def iter_qsort(array, start, stop):
    # Initialize the stack
    stack_size = stop - start + 1;
    stack = [0] * stack_size
    top = -1

    # Pushing the initial start, stop to stack
    top += 1
    stack[top] = start
    top += 1
    stack[top] = stop

    # If the stack is not empty pop the last call
    while top >= 0:
        stop = stack[top]
        top -= 1
        start = stack[top]
        top -= 1
        pi = partition(array, start, stop)

        # The left subarray [start, start + 1, ..., pi - 1] has more than one element 
        if pi - 1 > start:
            top += 1
            stack[top] = start
            top += 1
            stack[top] = pi - 1

        # The same for the right array
        if pi + 1 < stop:
            top += 1;
            stack[top] = pi + 1
            top += 1;
            stack[top] = stop


arr = [4, 3, 5, 2, 1, 3, 2, 3]
n = len(arr)
iter_qsort(arr, 0, n-1)
for i in range(n):
    print ("% d" % arr[i]),