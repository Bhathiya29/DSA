def euclidean_algorithm(a,b):
    while b!=0:
        a,b = b,a%b
    return a

a1, b1 = 56, 98
print(f"GCD of {a1} and {b1} is: {euclidean_algorithm(a1, b1)}")