def pattern_9(n):
    start = 1
    for i in range(n):
        if i%2 == 0 : 
                start = 0
        else : start =1
        for j in range(0,i):
            print(start,end = ' ')
            switch(start)
    
        print("")


        
def switch(n):
    if n == 0: return 1
    else: return 0

pattern_9(5)