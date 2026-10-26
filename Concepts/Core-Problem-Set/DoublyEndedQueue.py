class Node:
    def __init__(self, value = None):
        self.value = value
        self.prev = None
        self.next = None
    

class Deque:
    def __init__(self):
        self.left = Node()
        self.right =  Node()
        self.left.next = self.right
        self.right.prev = self.left

    def _insert_after(self,prev,node):
        node.prev = prev
        node.next = prev.next
        prev.next.prev = node
        prev.next = node
    
    def _remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node.value
    
    def push_front(self,value):
        self._insert_after(self.left , Node(value))

    def push_back(self,value):
        self._insert_after(self.right.prev, Node(value))

    def pop_front(self):
        if self.left.next == self.right:
            return None
        return self._remove(self.left.next)
    
    def pop_back(self):
        if self.right.prev == self.left:
            return None
        return self._remove(self.right.prev)
        