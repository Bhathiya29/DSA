from math import sqrt,floor

def is_prime(num):
    counter = 0

    if num < 2:
        return False

    for i in range (2,floor(sqrt(num))+ 1):
        if num%i == 0:
            counter += 1

    return counter == 1

number = 1

print(is_prime(number))