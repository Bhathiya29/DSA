import heapq

l1 = [10,20,30,40,50]
l2 = [15,25,35,45,55]

l3 = heapq.merge(l1,l2)

print(list(l3))