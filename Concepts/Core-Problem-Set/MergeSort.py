def merge_sort(nums):
    if len(nums) <=1:
        return nums
    
    mid = len(nums)//2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left,right)


def merge(left, right):
    sorted_arr =[]
    i=j=0

    while i < len(left) and j< len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i+=1
        else:
            sorted_arr.append(right[j])
            j+=1
    
    # Apepnding the left
    sorted_arr.append(left[i:])
    sorted_arr.append(right[j:])

    return sorted_arr
