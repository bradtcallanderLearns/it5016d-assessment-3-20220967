# LearningActivity32.py
# Author: Brad Callander
# Date: 11/11/2023

# This learning activity is practice for using boolean comparisons.

from datetime import date

# Challenge 1
birthyear = input("Please enter your year of birth: ")
name = input("Please enter your name: ")
current_year = (date.today().year)
print("The result of your application is",
str((current_year - int(birthyear) >= 21)
and name != "Suzanne May"
and name != "Wiremu Rangi"))