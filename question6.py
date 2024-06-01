# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, ithe f
# 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
# Return the resulting string

def find_substring(str1):
    string=str1.find("not")
    string1=str1.find("poor")
    if string1>string:
        if string>0 and string1>0:
            str1=str1.replace(str1[string:(string1+4)],"good")
            return str1
    else:
            return str1

str1=input("enter the string : ")
print(find_substring(str1))




