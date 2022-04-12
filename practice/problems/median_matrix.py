from math import floor, sqrt
from tkinter import N
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

def get_index(index, n):
    row = index // n
    col = index % n

def Median(T):
    length = len(T[0])


T = [ [ 2, 3, 5],
[ 7,11,13],
[17,19,23] ]
result = Median(T)
prt(result)
