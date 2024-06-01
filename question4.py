''' 4) Write a Python program to get a single string from two given strings, separated by a space and swap the first
two characters of each string.'''

def concat_str(a, b):
    a1 = b[:2] + a[2:]#here we swap the string first two latter

    b1 = a[:2] + b[2:]

    return a1 + ' '+b1
a=input("enter the string:> ")#user enter first string
b=input("enter the string:>")#here second string

print(concat_str(a, b))#here we call the function

