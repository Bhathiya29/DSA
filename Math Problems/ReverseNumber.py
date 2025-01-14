def reverse_number(number):
    reversed = 0
    while number % 10 !=0:
        val = number %10
        reversed = reversed*10 + val
        number = number // 10
        
    
    return reversed


print(reverse_number(7789))
