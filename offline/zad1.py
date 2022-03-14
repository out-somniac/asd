from zad1testy import Node, runtests
from math import floor

# Krzysztof Pęczek
# Program działa dzięki strukturze kopca. Ponieważ lista jest k-chaotyczna to w pierwszych k+1 Node'ach listy musi być element najmniejszy.
# Stworzona zostaje tablica k+1 wartości. Można za pomocą algorytmu Floyda do konstruowania kopca naprawić strukturę kopca w tablicy w czasie O(K)
# Kolejno wyciągany zostaje najmniejszy element z kopca w czasie O(log(k)) i dokładany zostaje kolejny z listy także w O(log(k)).
# Ta operacja jest powtarzana aż lista oraz kopiec nie mają elementów. Finalnie więc przeprowadzonych zostało n-k operacji o koszcie O(log(k))
# Dlatego złożoność tego algorytmu to O(nlog(k)) 

class Heap:
    def __init__(self, array, heap_size):
        self.size = heap_size
        self.array = array

        index = (self.size // 2) - 1
        while index >= 0: 
            self.Heapify(index)
            index -= 1

    def IsEmpty(self):
        return self.size <= 0

    def Extract(self):
        result = self.array[0]
        temp = self.array[0]
        self.array[0] = self.array[self.size - 1]
        self.array[self.size - 1] = temp
        self.size -= 1
        self.Heapify(0)
        return result

    def Insert(self, value):
        self.array[self.size] = value
        self.size += 1

        index = self.size - 1
        parent = floor(index - 1) // 2
        while parent >= 0 and self.array[parent] > self.array[index]:
            temp = self.array[index]
            self.array[index] = self.array[parent]
            self.array[parent] = temp

            index = parent
            parent = floor( index - 1) // 2

    def Heapify(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < self.size and self.array[left] < self.array[smallest]:
            smallest = left
        if right < self.size and self.array[right] < self.array[smallest]:
            smallest = right
        if smallest != index:
            temp = self.array[index]
            self.array[index] = self.array[smallest]
            self.array[smallest] = temp

            self.Heapify(smallest)

def SortH(p, k):
    heap = [0 for i in range(0, k+1)]
    heap_size = 0
    current = p
    for i in range(0, k+1):
        heap[i] = current.val
        current = current.next
        heap_size += 1
        if current == None:
            break

    heap = Heap(heap, heap_size)
    head = Node()
    tail = head
    tail.val = heap.Extract()
    if current != None:
        heap.Insert(current.val)
        current = current.next
        
    while current != None:
        tail.next = Node()
        tail = tail.next
        tail.val = heap.Extract()
        heap.Insert(current.val)
        current = current.next
    
    while not heap.IsEmpty():
        tail.next = Node()
        tail = tail.next
        tail.val = heap.Extract()
    
    return head

runtests( SortH ) 