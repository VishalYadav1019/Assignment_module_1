# Counting the frequencies in a list using a dictionary in Python.

l = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

d = {}

for i in l:#here i start the loop on l
    if i in d:#here the condition is if i in b then store in dictionary d
        d[i]+=1
    else:
        d[i]=1

print(d)#and in the last print d.



