#!/user/bin/env python3

# Script name Assignment 100 Days of  Python
# Author Name Christen Reinhart
# Date of Latest Revision 06/13/2024
# Sources Auditorium/ Udemy
# Purpose In Python, Fizz Buzz game

# For Loop with Range
target = 100


for number in range(1, target + 1,):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else
        print(number)
