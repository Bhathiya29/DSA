def merge_sort(arr):
    if len(arr) > 1:

        middle = len(arr)//2
        l = arr[:middle]
        r = arr[middle:]

        merge_sort(l)
        merge_sort(r)

        i=j=k = 0

        while i <len(l) and j < len(r):
            if l[i]<r[j]:
                arr[k] = l[i]
                i+=1
            else:
                arr[k] = r[j]
                j+=1
            k+=1

        
        while i< len(l):
            arr[k] = l[i]
            i+=1
            k+=1

        while j < len(r):
            arr[k]=r[j]
            j+=1
            k+=1



array = [6, 5, 12, 10, 9, 1]

merge_sort(array)

print("Sorted array is: ")
print(array)