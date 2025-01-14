import math

def is_prime(number):
    if number <= 1:
        return False  
    count = 0
    for i in range(1, math.isqrt(number) + 1):
        if number % i == 0:
            count += 1
        if count > 1:  
            return False
    return count == 1  

# Test cases 
print(is_prime(11))  
print(is_prime(36))  
