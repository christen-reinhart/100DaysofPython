#!/user/bin/env python3

# Script name Assignment 100 Days of  Python
# Author Name Christen Reinhart
# Date of Latest Revision 06/13/2024
# Sources Auditorium
# Purpose In Python, BMI Calculation

# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# Don't change the code above

# Write your code below this line
weight_as_int = int(weight)
height_as_float = float(height)

bmi = weight_as_int / (height_as_float * height_as_float)
bmi_as_int = int(bmi)
print(bmi_as_int)
