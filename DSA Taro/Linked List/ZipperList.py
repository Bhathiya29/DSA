class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next =b
b.next =c
c.next =d

e = Node(1)
f = Node(2)
g = Node(3)
h = Node(4)

e.next = f
f.next = g
g.next = h
 
def zip_list(head1,head2):
    tail = head1
    current1 = head1.next
    current2 = head2

    count = 0

    while current1 is not None and current2 is not None:
        if count%2 == 0:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next
        tail = tail.next
        count+=1

        if current 1 is not None: tail.next = current1
        if current 2 is not None: tail.next = current2

    return head1
