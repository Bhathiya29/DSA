import math

def print_all_divisions(number):
    for i in range(1, math.isqrt(number) + 1):
        if number % i == 0:
            print(i)
            if (number // i != i):
                print(number // i)

print_all_divisions(36)
