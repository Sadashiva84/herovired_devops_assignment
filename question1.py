# This is Q1 of the Assignment
'''
Question: In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. 
Create a Python script to check the password strength. 

●       Implement a Python function called check_password_strength that takes a password string as input.

●       The function should check the password against the following criteria:

○       Minimum length: The password should be at least 8 characters long.

○       Contains both uppercase and lowercase letters.

○       Contains at least one digit (0-9).

○       Contains at least one special character (e.g., !, @, #, $, %).

●       The function should return a boolean value indicating whether the password meets the criteria.

●       Write a script that takes user input for a password and calls the check_password_strength function to validate it.

●       Provide appropriate feedback to the user based on the strength of the password. 

'''
from colorama import Fore

def check_password_strength(password):
    pass_length = False
    strength = 1
    if len(password) > 8:
        print(Fore.GREEN + "Password is longer than 8 Characters")
        pass_length = True
        strength +=1

    lower_char = False
    upper_char = False
    num_char = False
    for char in password:
        if char.isdigit():
            num_char = True
            print(Fore.GREEN + "Contains Digits")
            strength +=1
            break

    for char in password:
        if char.islower():
            lower_char = True
            print(Fore.GREEN + "Contains 'lower' case character")
            strength +=1
            break

    for char in password:
        if char.isupper():
            upper_char = True
            print(Fore.GREEN + "Contains 'UPPER' case character")
            strength +=1
            break
    

    if pass_length == False:
        print(Fore.RED + "Password too short")
    if lower_char == False:
        print(Fore.RED + "No lower case found")
    if upper_char == False:
        print(Fore.RED + "No upper case found")

    spcl_char = False

    for char in password:

        if str(char) in ('!','@','#','$','%'):
            spcl_char = True
            print(Fore.GREEN + "Special Character Available")
            strength +=1
            break

    if spcl_char == False:
        print(Fore.RED + "No Special Character")

    if strength > 4:
        print(Fore.GREEN + "Password is Strong !!!")
    elif strength >2:
        print(Fore.LIGHTMAGENTA_EX + "Password  is Weak :(")
    else:
        print(Fore.RED + "Password is Poor! Warning")

password = input("\nPlease Enter A Password: ")

check_password_strength(password)



    