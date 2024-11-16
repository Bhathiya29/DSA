def pair_product(arr,target):
    previous = {}

    for i in range(0,len(arr)+1):
        complementary = target/arr[i]

        if complementary in previous:
            return previous[complementary],i
        else:
            previous[arr[i]]=i

    

array = [4,5,6,9,10,2]
targett = 60

print(pair_product(array,targett))