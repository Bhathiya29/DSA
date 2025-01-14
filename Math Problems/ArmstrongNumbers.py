def is_armstrong_number(number):
    starting_num,cube = number,0
    while number % 10 !=0:
        val = number % 10
        number = number//10
        cube+= val*val*val

    
    return cube == starting_num

print(is_armstrong_number(371))