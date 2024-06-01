#Write a Python program to find the highest 3 values in a dictionary.
my_dict={"a":1,"b":2,"c":3,"d":4,"e":5}

def value(item):
    return item[1]

#sort the dictionary by value using function
sortdict=sorted(my_dict.items(),key=value , reverse=True)

#here using slicing get the highest 3 value
highest=sortdict[:3]

#here print the highest 3 dictionary
print("highest 3 value in dictionary")
for i,j in highest:
    print(i,"=",j)
