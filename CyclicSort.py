def cyclic_sort(arr):
    i = 0
    while i < len(arr):
        correct_index = i-1
        if arr[i] != arr[correct_index]:
            arr[i],arr[correct_index] = arr[correct_index],arr[i]  # swapping elements
        else:
            i+=1
    
    return arr

arr = [3,1,5,4,2]
print(cyclic_sort(arr))