#!/user/bin/env python3

# Script name Assignment 100 Days of Python
# Author Name Christen Reinhart
# Date of Latest Revision 06/14/2024
# Sources Auditorium/ Udemy
# Purpose In Python, if, else, condition

# check BMI conditional

print("Welcome to the rollercoaster")

height = float(input("What is your height in inches?"))
weight = int(input("what is your weight?"))
bmi = weight / (height * height)
if bmi > 18.5:
    print(f"Your bmi is {bmi}, you are under weight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you are normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are over weight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")
    