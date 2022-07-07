# Implementation of an array based stack

MAX_SIZE = 64

class Stack():
    def __init__(self):
        self.size = 0
        self.values = [0] * MAX_SIZE
    
    def pop(self):
        if self.size <= 0:
            return None
        else:
            self.size -= 1
            return self.values[self.size]
    
    def push(self, value):
        try :
            self.values[self.size] = value
            self.size += 1
        except IndexError:
            pass
    
    def is_empty(self):
        return self.size == 0