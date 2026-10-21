from collections import deque


def binary_searh(arr, target):
    left,right = 0 , len(arr)-1

    while left <= right:
        mid = (left+right)//2

        if arr[mid]==target:
            return mid
        elif arr[mid] <target:
            right = mid -1
        else:
            left = mid+1
    return -1

def bfs(root):
    queue = deque([root])

    while len(queue) > 0:
        node = queue.popleft()

        for child in node.children:
            if is_goal(child):
                return FOUND(child)
            queue.append(child)
    
    return NOT_FOUND

def dfs(root, target):
    if root is None:
        return None
    if root.val == target:
        return root
    left = dfs(root.left, target)
    if left is not None:
        return left
    right = dfs(root.right,target)

