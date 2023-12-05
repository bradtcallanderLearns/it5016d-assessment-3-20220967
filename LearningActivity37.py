# LearningActivity37.py
# Author: Brad Callander
# Date: 13/11/2023

# This learning activity is practice for using while loops.

# Challenge 1
is_running = True
number = int(input("Enter a number: "))
counter = 0

while counter < number :
    print("[", counter + 1, "]", end="")
    counter += 1

# Challenge 2
number = int(input("Enter a number: "))
counter = 0
total = 0

while counter <= number :
    total = total + counter
    counter += 1

print("n = ", number, " sum = ", total)