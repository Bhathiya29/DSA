def check_palindrome(number):
    reversed_num = helper_reverse_number(number)

    return reversed_num == number
    


def helper_reverse_number(number):
    reversed = 0
    while number % 10 !=0:
        val = number %10
        reversed = reversed*10 + val
        number = number // 10
        
    
    return reversed


print(check_palindrome(5115))