#!/user/bin/env python3

# Script name Assignment 100 Days of  Python
# Author Name Christen Reinhart
# Date of Latest Revision 06/13/2024
# Sources Auditorium
# Purpose In Python, Calculate student height using Loops

student_heights = [160, 172, 168, 174, 169]  # Example data, replace with actual input if needed

total_height = 0 
for height in student_heights:
    total_height += height
print(f"total_height = {total_height}")

number_of_students = 0
for student in student_heights:
    number_of_students =+ 1
print(f"number of students = {number_of_students}") 

average_height = round(total_height / number_of_students) 
print(f"average height = {average_height}")  
    