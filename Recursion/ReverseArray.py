def reverse_arr(arr):
    if len(arr)<=1:
        return
    
    for i in range(len(arr)//2):
        arr[i],arr[len(arr)-i-1] = arr[len(arr)-i-1],arr[i]

    return arr

array = [1,2,3,4,5,6] 

print(reverse_arr(array))

def reverse_arr_recursion(arr,start = 0, end = None):
    if end is None:
        end = len(arr)-1
    
    if start >= end:
        return arr
    
    arr[start],arr[end] = arr[end],arr[start]

    reverse_arr_recursion(arr,start+1,end -1)