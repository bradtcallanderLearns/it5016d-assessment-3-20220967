# LearningActivity23.py
# Author: Brad Callander
# Date: 10/11/2023

# This learning activity is practice for using date and time.

from datetime import datetime
from datetime import timedelta

# Challenge 1
date_input = input("Please enter a date in the format DD Mmm YYYY:")
date_object = datetime.strptime(date_input, '%d %b %Y')
print("The date you entered is", date_object)
# Subtract 125 days from the date
print("That date 125 days earlier would have been", date_object - timedelta(days=125))

# Challenge 2
date_input = input("Please enter a date in the format DD Mmm YYYY:")
date_object = datetime.strptime(date_input, '%d %b %Y')
print("The date you entered is", date_object)
# Add 2 weeks to the date
print("That date 2 weeks later would be", date_object + timedelta(days=14))

# Challenge 3
birthdate_1 = input("Please enter the first birthdate in the format DD Mmm YYYY:")
birthdate_2 = input("Please enter the second birthdate in the format DD Mmm YYYY:")
date_object_1 = datetime.strptime(birthdate_1, '%d %b %Y')
date_object_2 = datetime.strptime(birthdate_2, '%d %b %Y')
print("The birthdates you entered are", date_object_1, "and", date_object_2)
# Calculate the age difference of the two birthdates
age_difference = date_object_1 - date_object_2
print("The age difference is", abs(age_difference.days), "days")

# Challenge 4
print("Welcome to this simple date calculator!")
date_input = input("Please enter a date in the format DD Mmm YYYY:")
number_input = int(input("Please enter a number which represents an amount of years:"))
date_object = datetime.strptime(date_input, '%d %b %Y')
# Add the number of years to the date
new_date = date_object + timedelta(days = 365.25 * number_input)
print(new_date)

# Challenge 5
date_input_1 = input("Please enter the first date in the format DD Mmm YYYY:")
date_input_2 = input("Please enter the second date in the format DD Mmm YYYY:")
date_object_1 = datetime.strptime(date_input_1, '%d %b %Y')
date_object_2 = datetime.strptime(date_input_2, '%d %b %Y')
# Calculate the difference in years
date_difference = date_object_1 - date_object_2
years_difference = abs(round(date_difference.days / 365.25))
print("The date difference is", years_difference, "years")