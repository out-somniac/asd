# Implementation of a dynamic stack

class Stack():
    def __init__(self):
        self.values = [0] * 4 # 4 is just a hardcoded starting size
        self.top = -1
        self.size = 4

    def push(self, value):
        if self.top < self.size - 1:
            self.top += 1
            self.values[self.top] = value
        else:
            # Here the resizing happens
            self.size = 2 * self.size
            new_array = [0] * self.size
            for i in range(0, self.size // 2):
                new_array[i] = self.values[i]
            self.values = new_array
            self.top += 1
            self.values[self.top] = value

    def pop(self):
        if self.top < self.size // 2 and self.size > 4:
            self.size = self.size // 2
            new_array = [0]*self.size
            for i in range(self.size):
                new_array[i] = self.values[i]
            self.values = new_array
            result = self.values[self.top]
            self.top -= 1
            return result
        else:
            result = self.values[self.top]
            self.top -= 1
            return result
    def is_empty(self):
        return self.top <= 0