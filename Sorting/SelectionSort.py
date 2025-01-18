def selection_sort(arr):
    for step in range(len(arr)):
        min_index = step

        for i in range(step+1,len(arr)):
            if arr[i]< arr[min_index]:
                min_index = i
        
        arr[step],arr[min_index]=arr[min_index],arr[step]


array_data = [-2, 45, 0, 11, -9]

selection_sort(array_data)

print(array_data)