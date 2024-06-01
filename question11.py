#Write a Python program to unzip a list of tuples into individual list
d=[]#here we declare the blank list
a=[]
b=[]

list=[("vishal",1),("anvesh",2),("ayushi",3),("vivek",4)]

print("original list : ",str(list)) #first we print the original list

for i in list: #we put the condition on the list
    a.append(i[0])#here we add 0 index value in the a
    b.append(i[1])#and 1 index value in the b

d.append(tuple(a))#here we can store the value in the d
d.append(tuple(b))

print("unzip list : ",d)#here we print the d


