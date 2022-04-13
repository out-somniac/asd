# Find length of longest increasing subsequence

def lis(array):
    n = len(array)
    F = [1 for i in range(n)] # Stores values of lis untill index i
    max_index = 0

    for i in range(1, n):
        for j in range(0, i):
            if array[i] > array[j] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
        if F[i] > F[max_index]:
            max_index = i
    return F[max_index]


def print_lis(array):
    n = len(array)
    F = [1 for i in range(n)] # Stores values of lis untill index i
    max_index = 0

    parent = [-1 for i in range(n)]

    for i in range(1, n):
        for j in range(0, i):
            if array[i] > array[j] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                parent[i] = j
        if F[i] > F[max_index]:
            max_index = i

    print_sol(array, parent, max_index)

def print_sol(array, parent, index):
    if parent[index] != -1:
        print_sol(array, parent, parent[index])
    print(array[index])