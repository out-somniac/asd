from math import floor, sqrt
def partition(array, start, stop):
    pass

def select(array, start, stop, k):
    if start == stop:
        return array[start]
    if start < stop:
        pi = partition(array, start, stop)
        if pi == k:
            return array[pi]
        elif k < pi:
            return select(array, start, pi - 1, k) 
        else:
            return select(array, pi + 1, stop, k)  


def prt(array):
    for row in array:
        for val in row:
            print(val, end=", ")
        print("")
    print("")

def linearize(T):
    n = len(T)
    array = [0]*n*n
    for i in range(len(T)):
        for j in range(len(T[0])):
            array[i*n + j] = T[i][j]
    array.sort()
    return array

def Median(T):
    sorted = linearize(T)
    print(sorted)
    n = len(T[0])
    result = [[0 for i in range(n)] for j in range(n)]
    for i, val in enumerate(sorted):
        if i < (n * n - n) // 2:
            row = floor((sqrt(1+8*i) - 1 ) / 2) + 1
            col = (row * (row + 1) // 2) - i - 1
            result[row][col] = val
        elif i >= (n * n + n) // 2:
            j = i - ((n * n + n) // 2)
            col = floor((sqrt(1+8*j) - 1 ) / 2) + 1
            row = (col * (col + 1) // 2) - j - 1
            result[row][col] = val
        else:
            index = i - (n*n - n)//2
            result[index][index] = val
    return result


T = [ [ 2, 3, 5],
[ 7,11,13],
[17,19,23] ]
result = Median(T)
prt(result)
