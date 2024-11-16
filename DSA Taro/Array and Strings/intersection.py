def intersection(arr1,arr2):
    elements = set(arr1)

    section = []

    for i in arr2:
        if i in elements:
            section.append(i)
        
    
    return section

a1 = [1,3,5,7,6]
a2=[5,8,9,2,7]

print(intersection(a1,a2))

