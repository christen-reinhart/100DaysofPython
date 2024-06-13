#!/user/bin/env python3

# Script name Assignment 100 Days of  Python
# Author Name Christen Reinhart
# Date of Latest Revision 06/13/2024
# Sources Auditorium/ Udemy
# Purpose In Python, Password Generator

# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')']


print("Welcome to the Password Gengerator")
nr_letters = int(input("How many letter would you like in password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many number would you like?\n"))

# Eazy Level
password = ""
# nr_letter = 4
for char in range(1, nr_letters + 1):
    # 1 - 4
    random_char = random.choice(letters)
    password += random_char
    print(password)








