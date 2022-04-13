class ShiftQueue():
    def __init__(self):
        self.values = [0] * 64
        self.first = 0
        self.size = 0
    
    def push(self, value):
        if self.first + self.size == len(self.values):
            if self.first == 0:
                return # The queue is full
            else:
                target_index = 0
                for i in range(self.first, self.first + self.size):
                    self.values[target_index] = self.values[i]
                    target_index += 1
        else:
            self.values[self.first + self.size] = value
            self.size += 1

    def pop(self):
        if self.size <= 0:
            return
        else:
            self.size -= 1
            result = self.values[self.first]
            
            if self.size == 0:
                self.first = 0
            else:
                self.first += 1
            return result

    def is_empty(self):
        return self.size == 0
