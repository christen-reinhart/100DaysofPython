#!/user/bin/env python3

# Script name Assignment 100 Days of  Python
# Author Name Christen Reinhart
# Date of Latest Revision 06/14/2024
# Sources Auditorium/ Udemy
# Purpose In Python, if, else, condition

# Multiple If Statements

print("Welcome to Python Pizza")
size = int(input("What is your size pizza? S, M, L"))
add_pepperoni = int(input("Do you want pepperoni? Y or N"))
add_cheese = int(input("Do you want cheese? Y or N"))

bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}."