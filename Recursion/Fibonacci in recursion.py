def fib_recurssion(num):
    if num<=1:
        return num
    
    last = fib_recurssion(num-1)
    slast = fib_recurssion(num-2)

    return last+slast

print(fib_recurssion(3))