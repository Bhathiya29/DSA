def pattern_5(n):
    for i in range(n,0,-1):
        for j in range(0,i):
            print(j,end='')
        print("")        


pattern_5(5)