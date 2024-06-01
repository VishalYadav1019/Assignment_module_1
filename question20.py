import string
import random

# Getting password length
length = int(input("Enter password length: "))

print('''Choose character set for password from these : 
		1. Digits
		2. Letters
		3. Special characters
		4. Exit''')

characterList = ""

# Getting character set for password
while True:
    choice = int(input("choice a number "))
    if (choice == 1):

        # Adding letters in a password
        characterList += string.ascii_letters
    elif (choice == 2):

        # Adding a digits in password
        characterList += string.digits
    elif (choice == 3):

        # Adding special characters in password
        characterList += string.punctuation
    elif (choice == 4):
        break
    else:
        print("Invalid Choice!")

password = []

for i in range(length):
    # Picking a random character from our
    # character list
    randomchar = random.choice(characterList)

    # appending a random character to password
    password.append(randomchar)

print("The random password is " + "".join(password))





