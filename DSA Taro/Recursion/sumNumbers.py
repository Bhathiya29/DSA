def sum_numbers_recursive(numbers):
    if len(numbers) ==0:
        return 0
    
    return numbers[0] + sum_numbers_recursive(numbers[1:])

nums = [2,5,6,9]

print(sum_numbers_recursive(nums))