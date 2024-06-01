''' 5) Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead If the string length of the given
string is less than 3, leave it unchanged'''

str=input("enter the string : ")

if len(str)<3:#if the string length is less then 3 then print the string which user enter
    print(str)

elif str[-3:]=="ing":#if the string last 3 latter is ing then add ly on the string
    print(str + "ly")

else :
    print(str + "ing")#if the string last 3 latter is not ing then add ing.
