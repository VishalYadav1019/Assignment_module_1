#Write a Python function that takes a list and returns a new list with unique elements of the first list
def uniquelist(l):
    l1=[]#here i declare a blank list where the unique value is store
    for i in l:
        if i not in l1:#here i gave the condition if i not in l1 then i store in l1
            l1.append(i)
    for i in l1:#here i start the second loop if i in l1 then print i
        print(i)

l=[1,2,5,4,3,6,4,7,6,5,3]#here i declare the list
uniquelist(l)#here i call the function