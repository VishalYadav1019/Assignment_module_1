#Write a Python program to get unique values from a list.


l=[1,2,32,7,23,21,2,1,3,4,2,4,6,8]
l.sort()
print(l)

l1=[]

for i in l:#here we start the loop on the l.
    if i not in l1:#we put the condition l not in l1 then print i this take only unique value

        l1.append(i)#here the value store from backside of the list

    else:
        pass

print(l1)
