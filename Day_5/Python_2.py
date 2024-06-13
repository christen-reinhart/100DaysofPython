#!/user/bin/env python3

# Script name Assignment 100 Days of  Python
# Author Name Christen Reinhart
# Date of Latest Revision 06/13/2024
# Sources Auditorium
# Purpose In Python, Loops

# Input a list student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    
highest_score = 0 
for score in student_scores:
    if score > highest_score:
        highest_score = score
        # print(highest_score)
        
print(f"The highest score in the class is: {highest_score}")