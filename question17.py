#Write a python program using function to find the sum of odd series and even series
evcount=0
odcount=0
evsum=0
odsum=0
for i in range(1,6,1):
    n=eval(input("enter the number..."))

    if n%2==0:
        print("number is even")
        evcount+=1
        evsum+=n

    else:
        print("number is odd")
        odcount+=1
        odsum+=n



print("even numbers are: ",evcount)
print("odd numbers are: ",odcount)
print("sum of even number : ",evsum)
print("sum of odd number :",odsum)