# implementing a hash map from scratch

class HashMap:
    def __init__(self,size =10):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def hash_function(self,key):
        return hash(key) % self.size
    
    def insert(self,key,value):
        index = self.hash_function(key)
        # handling collisions by appending to the list at the index
        for i,(k,v) in enumerate(self.table[index]):
            if k == key: #key exists, update value
                self.table[index][i] = (key,value)
                return
        self.table[index].append((key,value)) # Adds the new key value pair

    def search(self,key):
        index = self.hash_function(key)
        for k,v in self.table[index]:
            if k == key:
                return v
        return None
    
    def delete(self,key):
        index = self.hash_function(key)
        for i,(k,v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return
        print("key not found")


# Test 
hash_map = HashMap()
hash_map.insert("apple", 10)
hash_map.insert("banana", 20)
print(hash_map.search("apple"))  # Output should be: 10
hash_map.delete("apple")
print(hash_map.search("apple"))  # Output should be: None
