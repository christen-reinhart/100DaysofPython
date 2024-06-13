#!/user/bin/env python3

# Script name Assignment 100 Days of  Python
# Author Name Christen Reinhart
# Date of Latest Revision 06/13/2024
# Sources Auditorium
# Purpose In Python, Calculate Bill

# Welcome to bill calculator
print("Welcome to the trips calculator")

#Each person should pay
bill = float(input("What was the total bill?$"))

# Calculate Tip
tip = int(input("How much would you like to give? 10, 12, or 15?"))

# How many people 
people = int(input("How many people split the bill?"))

bill_with_tip = tip / 100 * bill + bill

print(bill_with_tip)
