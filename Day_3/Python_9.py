#!/user/bin/env python3

# Script name Assignment 100 Days of Python
# Author Name Christen Reinhart
# Date of Latest Revision 06/14/2024
# Sources Auditorium/ Udemy
# Purpose In Python, if, else, and, or, not

# Logical Operators

print("Welcome to the rollercoaster")

height = int(input("What is your height in inches?"))
age = int(input("What is your age?"))
if height >= 48:
    print("You can ride the rollercoaster!")
    age = int(input("what is your age?"))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. You get to ride for free.")
    else:
        print("Please pay $12.")   
else:
    print("Sorry, you will have to wait till you are taller")     
