def pair_sum(arr,sum):
    pairs ={}

    for i in range(0,len(arr)+1):
        complementary = sum - arr[i]
        if complementary in pairs:
            return pairs[complementary],i
        
        else:
            pairs[arr[i]]=i
        

array = [1,4,5,3,7]
summ =8

print(pair_sum(array,summ))
