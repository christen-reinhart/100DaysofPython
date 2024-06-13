#!/user/bin/env python3

# Script name Assignment 100 Days of  Python
# Author Name Christen Reinhart
# Date of Latest Revision 06/13/2024
# Sources Auditorium/ Udemy
# Purpose In Python, perform range using Loops

# For Loop with Range
target = int(input()) # Number between 0 and 1000

even_sum = 0

for number in range(2, target + 1, 2):
    # accumulate even_sum here
    even_sum += number
print(even_sum)
