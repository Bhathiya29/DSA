def count_digits(number):
    count = 0
    while number % 10 !=0:
        val = number %10
        number = number // 10
        count +=1
    
    return count


print(count_digits(7789))

# Time complexity = Log(n)