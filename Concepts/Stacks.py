# Stacks

stack = []

stack.append(1)
stack.append(2)
stack.append(3)

x = stack.pop()

print(stack)

if stack:
    stack.pop()

# Queues
from collections import deque

q = deque()

q.append(1)
q.append(2)
q.append(3)

q.popleft()
q.popleft()

y = q[0]

