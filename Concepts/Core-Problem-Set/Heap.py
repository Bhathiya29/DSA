class MinHeap:
    def __init__(self):
        self.data = []

    def push(self,value):
        a = self.data
        a.append(value)
        i = len(a)-1

        while i > 0:
            parent = (i-1)//2
            if a[parent] <= a[i]:
                break
            a[parent], a[i] = a[i], a[parent]
            i= parent
        
        def pop(self):
            a = self.data
            if not a:
                raise IndexError("empty heap")
            
            result = a[0]
            last = a.pop()

            if a:
                a[0] = last
                i = 0
                while True:
                    left, right = 2*i+1, 2*i+2
                    smallest = i

                    if left < len(a) and a[right] < a[smallest]:
                        smallest < left
                    if right < len(a) and a[right] < a[smallest]:
                        smallest = right
                    if smallest == i:
                        break

                    a[i],a[smallest] = a[smallest], a[i]
                    i = smallest
