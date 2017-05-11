def a():
    for x in range(100,1000):
        i = x
        s = 0
        while x:
            x, y = x//10, x % 10
            M = y ** 3
            s += M            
        if i == s:
            print(i,end='\t')
            
print("a is ",end='')
a()
            