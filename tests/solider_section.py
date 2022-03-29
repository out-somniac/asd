# Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
# podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
# wzrostu. Proszę zaimplementować funkcję:
# section(T,p,q)
# która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
# powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
# algorytmu oraz proszę oszacować jego złożoność czasową

from math import floor
from random import randint

def heapify(array, size, index):
    smallest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < size and array[left] < array[smallest]:
        smallest = left
    if right < size and array[right] < array[smallest]:
        smallest = right
    if smallest != index:
        array[index], array[smallest] = array[smallest], array[index]
        heapify(array, size, smallest)

def build_heap(array):
    for i in range(floor(len(array) // 2), -1, -1):
        heapify(array, len(array), i)

def section(T, p, q):
    result = [0 for i in range(q-p+1)]

    size = len(T)
    build_heap(T)
    for i in range(0, p):
        size -= 1
        T[0], T[size] = T[size], T[0]
        heapify(T, size, 0)
    for i in range(q - p + 1):
        size -= 1
        result[i] = T[0]
        T[0], T[size] = T[size], T[0]
        heapify(T, size, 0)
    return result

