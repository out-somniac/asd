from math import floor

class Heap:
    def __init__(self, size):
        self.size = size
        self.array = [0 for i in range(size)]

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