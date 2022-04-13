# Find length of longest increasing subsequence

def lis(array):
    n = len(array)
    F = [1 for i in range(n)] # Stores values of lis untill index i
    max_index = 0

    for i in range(1, n):
        for j in range(0, i):
            if array[i] > array[j]:
                F[i] = max(F[i], F[j] + 1)
        if F[i] > F[max_index]:
            max_index = i
    return F[max_index]
