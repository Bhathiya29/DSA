class HashTable:
    def __init__(self,capacity = 16):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]

    def _bucket(self,key):
        return hash(key)% self.capacity
    
    def put(self,key,value):
        bucket = self.buckets[self._bucket(key)]
        for i, (k,_) in enumerate(bucket):
            if k == key:
                bucket[i] = (key,value)
                return
            
        bucket.append((key,value))
    
    def get(self,key):
        bucket = self.buckets[self._bucket(key)]
        for k, v in bucket:
            if k ==  key:
                return v
        
        return None
    
    def remove(self, key):
        bucket = self.buckets[self._bucket(key)]
        for i, (k,_) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return True
        return False
