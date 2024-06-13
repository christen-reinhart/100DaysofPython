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
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
bill_with_tip = tip / 100 * bill + bill

print(f"Each person should pay: ${final_amount}")
