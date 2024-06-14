#!/user/bin/env python3

# Script name Assignment 100 Days of  Python
# Author Name Christen Reinhart
# Date of Latest Revision 06/14/2024
# Sources Auditorium/ Udemy
# Purpose In Python, if, else, condition

# check leap year conditional

print("Welcome to the rollercoaster")

height = float(input("What is your height in inches?"))
year = int(input("what is the year?"))

if year % 4 == 0: 
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not leap year")
    else: 
        print("Leap Year")
else:
    print("Not a Leap Year")
    
