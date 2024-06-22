def square_sorted(arr):
    res = []

    l,r = 0,len(arr)-1
    while l <= r:
        if arr[l]*arr[l] < arr[r]*arr[r]:
            res.append(arr[r]*arr[r])
            r-=1
        else:
            res.append(arr[l]*arr[l])
            l+=1

    return res[::-1] #reverse


array = [-4,-3,0,1,10]
print(square_sorted(array))