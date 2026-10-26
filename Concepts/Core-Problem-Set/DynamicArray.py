"""
Implement an array that can grow when its capacity is reached, supporting operations such as get, set, pushback, popback, and resize.
"""

class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.data = [None]*self.capacity


    def get(self,i):
        if i < 0 or i>=self.size:
            raise IndexError("Index out of range")
        return self.data[i]
    
    def set(self,i,value):
        if i <0 or i>=self.size:
            raise IndexError("Index out of range")
        self.data[i] = value
    
    def pushback(self,value):
        if self.size == self.capacity:
            self.resize(self.capacity*2)
        self.data[self.size] = value
        self.size +=1
    
    def popback(self):
        if self.size == 0:
            raise IndexError("empty error")
        value = self.data[self.size-1]
        self.size-=1
        self.data[self.size] = None
        return value

