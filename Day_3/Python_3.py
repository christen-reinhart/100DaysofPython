#!/user/bin/env python3

# Script name Assignment 100 Days of  Python
# Author Name Christen Reinhart
# Date of Latest Revision 06/14/2024
# Sources Auditorium/ Udemy
# Purpose In Python, if, else, condition

# check height conditional

print("Welcome to the rollercoaster")

height = int(input("What is your height in inches?"))

if height >= 48:
    print("You can ride the rollercoaster!")
    age = int(input("what is your age?"))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")   
else:
    print("Sorry, you will have to wait till you are taller")     
