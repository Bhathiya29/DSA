# Min  Heap

A = [-4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

import heapq
heapq.heapify(A)

A

# Heap Push
heapq.heappush(A,4)

#  heap Pop
min = heapq.heappop(A)

heapq.heappoppush(A, 5)

# heap sort
def heap_sort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_arr = [0]*n

    for i in range(n):
        minn = heapq.heappop(arr)
        new_arr[i] = minn

    return new_arr


B = [4, 10, 3, 5, 1]

n = len(B)

for i in range(n):
    B[i] = -B[i]

heapq.heapify(B)

largest = -heapq.heappop(B)

print(largest)

heapq.heappush(B, -7)

# Building from Scratch

c = [-5, 2, 3, 1, 4,7]

heap = []

for x in c:
    heapq.heappush(heap,x)
    print(heap)

D = [5,3,3,5,4,1,2,2,1, 4,5,6,7,8,9]

from collections import Counter

counter = Counter(D)

heap = []

for k,v in counter.items():
    heapq.heappush(heap,(v,k))




