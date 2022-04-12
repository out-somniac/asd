# Implementation of a stack using a single linked list

class Node():
    def __init__(self, value):
        self.next = None
        self.value = value

class Stack():
    def __init__(self):
        self.head = None
    
    def push(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head == None:
            return None
        else:
            result = self.head.value
            self.head = self.head.next
            return result

    def is_empty(self):
        return self.head == None
