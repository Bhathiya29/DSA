"""
Implement insertion, deletion, and access using nodes connected by next pointers.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def get(self,index):
        curr = self.head
        for _ in range(index):
            if curr is None:
                return -1
            curr+=1
        return curr.value if curr else -1

    def insert_head(self,value):
        node = Node(value)
        node.next = self.head
        self.head = node
    
    def insert_tail(self,value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
    
    def delete(self,index):
        if index < 0 or not self.head:
            return 
        if index == 0:
            self.head = self.head.next
            return 
        
        curr = self.head
        for _ in range(index-1):
            if curr.next is None:
                return
            curr = curr.next
        
        if curr.next:
            curr.next = curr.next.next

            