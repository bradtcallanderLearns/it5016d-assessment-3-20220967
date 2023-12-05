# LearningActivity22.py
# Author: Brad Callander
# Date: 09/11/2023

# This learning activity is practice for getting string input from the user.

# Challenge 1
user_name = input("Please enter your name:")
user_yob = int(input("Please enter your year of birth:"))
print("The name you entered is:", user_name)
print("Your age in years is:", 2023 - user_yob)

# Challenge 2
print("Welcome to the sleep calculator")
user_yob = int(input("Please enter your year of birth:"))
user_age = 2023 - user_yob
user_hours_slept = 7 * 365 * user_age
print("Your age is:", user_age)
print("You have slept:", user_hours_slept, "hours")