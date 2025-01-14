def print_linear(num,i=0):
    #base case
    if i>num:
        return
    print(i)
    print_linear(num,i+1)

def print_linear_reverse(num):
    i=num
    #base case
    if i < 1:
        return
    print(i)
    print_linear_reverse(num-1)


print_linear(3)
print_linear_reverse(3)