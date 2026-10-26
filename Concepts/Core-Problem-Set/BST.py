"""
Implement insertion, search, and deletion while preserving the ordering property.
"""

class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def search(self, value):
        curr = self.root
        while curr:
            if curr.val == value:
                return True
            curr = curr.left if value<curr.val  else curr.right
        return False
    
    def insert(self,value):
        def add(node):
            if not node:
                return TreeNode(value)

            if value < node.val:
                node.left = add(node.left)
            elif value> node.val:
                node.right = add(node.right)
            return node
        self.root = add(self.root)

    def delete(self,value):
        def remove(node,value):
            if not node:
                return None
            if value < node.val:
                node.left = remove(node.left ,value)
            elif value > value.val:
                node.right = remove(node.right, value)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                successor = node.right
                while successor.left:
                    successor = successor.left
                node.val = successor.val
                node.right = remove(node.right, successor.val)
            return node
        
        self.root = remove(self.root, value)
