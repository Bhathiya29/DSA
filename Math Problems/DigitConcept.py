# extract all the digits out in backward manner

def extract_digits(number):
    digit = number
    while digit % 10 != 0:
        val = digit % 10
        digit = digit //10
        print(val)
        


print(extract_digits(7789))