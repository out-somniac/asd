from kol1btesty import runtests

# Dwa słowa są anagramami jeśli składająsię z dokładnie tej samej liczby tych samych liter. 
# Na przykład anagramami są słowa "algorytm" i "logarytm", podczas gdy słowa "katar" i "totem" anagramami ni są. 
# Jeśli dwa słowa są anagramami, to sa tej samej długości.
# Dana jest tablica T skaładająca się z pewnej liczby słów, gdzie każde słowo skłąda sięz małych liter alfabetu łącińskiego.
# Popularnością anagamową słowa T[i]nazywamy liczbę takich indeksów j, że słowo T[j] jest anagramem słowa T[i]
# Prosze zaimplementować funckcję f(T), która zwraca popularność najpopularniejszego anagramu.

# Progi: N - łączna długość napisów w tablicy wejściowej
# Pierwszy: O(Nlog(N))
# Drugi: O(N)

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0

    def append(self, value):
        self.size += 1
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
    
    def get_array(self):
        result = ["_" for _ in range(self.size)]
        curr = self.head
        index = 0
        while curr != None:
            result[index] = curr.value
            index += 1
            curr = curr.next
        return result

    def print_list(self):
        curr = self.head
        while curr != None:
            print(curr.value, " -> ", sep="", end="")
            curr = curr.next
        print("None")

def longest_series(array):
    max_length = 1
    for i in range(0, len(array) - 1):
        length = 1
        while i < len(array) - 1 and array[i] == array[i + 1]:
            length += 1
            i += 1
        if length > max_length:
            max_length = length
    return max_length

def min_max_len(array):
    min_len = float('inf')
    max_len = 0
    for word in array:
        if len(word) > max_len:
            max_len = len(word)
        if len(word) < min_len:
            min_len = len(word)
    return min_len, max_len

def alpha_sort(word):
    length = len(word)
    counts = [0 for i in range(26)]

    for letter in word:
        index = ord(letter) - ord('a')
        counts[index] += 1
    
    for i in range(1, 26):
        counts[i] += counts[i - 1]
    
    output = ['_' for _ in word]
    for i, letter in enumerate(word):
        index = ord(letter) - ord('a')
        output[counts[index] - 1] = letter
        counts[index] -= 1
    
    final = ""
    for letter in output:
        final += letter
    return final

def count_sort(array, place):
    length = len(array[0])
    counts = [0 for i in range(26)]

    for word in array:
        index = ord(word[place]) - ord('a')
        counts[index] += 1

    for i in range(1, 26):
        counts[i] += counts[i - 1]

    output = [None for _ in array]
    for i, word in enumerate(array):
        index = ord(word[place]) - ord('a')
        output[counts[index] - 1] = array[i]
        counts[index] -= 1

    for i in range(len(array)):
        array[i] = output[i]        


def radix_sort(array):
    if len(array) == 0:
        return

    length = len(array[0])
    place = length - 1
    while place >= 0:
        count_sort(array, place)
        place -= 1

def f(T):
    min_len, max_len = min_max_len(T)
    buckets = [LinkedList() for i in range(min_len, max_len + 1)]
    
    for word in T:
        buckets[len(word) - min_len].append(alpha_sort(word))
    
    largest = 1
    for bucket in buckets:
        sorted = bucket.get_array()
        radix_sort(sorted)
        
        result = longest_series(sorted)
        if result > largest:
            largest = result
    
    return largest

runtests( f, all_tests=True )