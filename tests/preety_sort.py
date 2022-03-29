
# ZADANIE
# 
# Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie
# jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. Mówimy,
# że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej
# cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta
# liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od
# 455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
# Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję:
# pretty_sort(T)
# która sortuje elementy tablicy T od najładniejszych do najmniej ładnych. Użyty algorytm
# powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
# algorytmu oraz proszę oszacować jego złożoność czasową.

def get_numbers(number):
    counts = [0]*10
    while number > 0:
        digit = number % 10
        number  = number // 10
        counts[digit] += 1
    singles = 0
    multiples = 0
    for c in counts:
        if c == 1:
            singles += 1
        elif c > 1:
            multiples += 1
    return singles, multiples

def is_less(a, b):
    a_singles, a_multiples = get_numbers(a)
    b_singles, b_multiples = get_numbers(b)

    if a_singles == b_singles:
        return a_multiples > b_multiples
    else:
        return a_singles < b_singles

def partition(array, start, stop):
    pivot = array[stop]
    i = start - 1
    for j in range(start, stop):
        if is_less(array[j], pivot):
            i += 1
            array[i], array[j] = array[j], array[i]
    i += 1
    array[i], array[stop] = array[stop], array[i]
    return i

def quick_sort(array, start, stop):
    if start > stop:
        return
    
    pi = partition(array, start, stop)
    quick_sort(array, start, pi - 1)
    quick_sort(array, pi + 1, stop)

def preety_sort(T):
    quick_sort(T, 0, len(T) - 1)