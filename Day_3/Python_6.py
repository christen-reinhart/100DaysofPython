#!/usr/bin/env python3

# Script name: Assignment 100 Days of Python
# Author Name: Christen Reinhart
# Date of Latest Revision: 06/14/2024
# Sources: Auditorium/ Udemy
# Purpose: In Python, if, else, condition

# Multiple If Statements

print("Welcome to Python Pizza")
size = input('What size pizza do you want? (S, M, L): ').upper()
add_pepperoni = input('Do you want pepperoni? (Y/N): ').upper()
add_cheese = input('Do you want extra cheese? (Y/N): ').upper()

bill = 0

# Calculate base price based on pizza size
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid size selected.")

# Add cost for pepperoni if selected
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size in ["M", "L"]:
        bill += 3

# Add cost for extra cheese if selected
if add_cheese == "Y":
    bill += 1

# Print the final bill
print(f"Your final bill is: ${bill}.")
