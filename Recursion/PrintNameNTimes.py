def print_name(num,i=0):
    #base case
    if i > num:
        return
    print("John Doe")
    print_name(num,i+1)

print_name(3)