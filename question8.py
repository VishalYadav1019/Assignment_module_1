#Write a Python program to check whether a list contains a sublist.
l=[1,2,3,2323,9,13,442,21,24,2,3]
print(l)

l1=[12,23,23,3]

for i in l1: # first we start the loop on l1
    if i in l:# here we give the condition if i in the l1 then print true otherwise print false.
        print("true")
    else:
        print("false")