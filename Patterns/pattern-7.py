def pattern_7(n):
    for i in range(n,0,-1):
        #space
        for j in range(n-i):
            print(" ",end='')
        #star
        for j in range(2*i-1):
            print("*",end='')
        #space
        for j in range(n-i):
            print(" ",end='')
        print("")

pattern_7(5)