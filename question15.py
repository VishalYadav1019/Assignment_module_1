n=7
a=0
b=1
if n==1:#if the number is 1 then the loop print the value of a
    print(a)
else:
    print(a)
    print(b)
    for i in range(2, n + 1):#here we start the loop end to 7
        c=a+b#here we take a new variable for adding the a and b
        a=b
        b=c
        print(c)




