import math
#greatest common denometer | Highest common factor

def gcd(num1,num2):
    # +1 to make sure the value is also included
    for i in range(1,min(num1,num2)+1):
        if(num1%i == 0 and num2%i ==0):
            gcd_val = i

    return gcd_val

print(gcd(24,12))