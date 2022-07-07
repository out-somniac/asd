# Impleentation of a priority queue using a heap and a dynamic resizing scheme

from math import floor
from random import randint

class PriorityQueue():
    def __init__(self):
        self.values = [0] * 4
        self.size = 0

    def __heapify(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < self.size and self.values[left] < self.values[smallest]:
            smallest = left
        if right < self.size and self.values[right] < self.values[smallest]:
            smallest = right
        if smallest != index:
            self.values[smallest], self.values[index] = self.values[index], self.values[smallest]
            self.__heapify(smallest)
    
    def pop(self):
        if self.size == 0:
            return

        result = self.values[0]
        self.size -= 1
        self.values[0], self.values[self.size] = self.values[self.size], self.values[0]
        self.__heapify(0)
        return result

    def push(self, value):
        if self.size >= len(self.values):
            new_array = [0]*2*self.size
            for i, elem in enumerate(self.values):
                new_array[i] = elem
            self.values = new_array
        self.values[self.size] = value
        self.size += 1
        index = self.size - 1
        parent = floor((index - 1) / 2)
        while self.values[parent] > self.values[index]:
            self.values[parent], self.values[index] = self.values[index], self.values[parent]
            index = parent
            parent = floor((index - 1) / 2)
    
    def is_empty(self):
        return self.size == 0