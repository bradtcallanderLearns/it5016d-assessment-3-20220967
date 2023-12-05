# LearningActivity33.py
# Author: Brad Callander
# Date: 11/11/2023

# This learning activity is practice for using if statements.

from datetime import datetime

# Challenge 1
print("Parking meter")
park_time = int(input("Enter how long you wish to park for: "))
print("park_time time is ", park_time, "hours")
rate = 4
cost = 0
if park_time > 3 :
    cost = rate * 3
    # reduce the rate to $2
    rate -= 2
    # get the remainder of the parking time
    park_time -= 3
    # add to the current cost
    cost += rate * park_time
    print("The cost of the parking is $", cost)
else :
    cost = rate * park_time
    print("The cost of the parking is $", cost)

# Challenge 2
score = 0
start_time = datetime.today()

question_1 = input("What is the capital city of New Zealand? ")
if question_1.lower() == "wellington" :
    score = score + 1
    print("That is correct! Your current score is:", score)
else :
    print("That is incorrect! Your current score is:", score)

question_2 = input("What is the name of the New Zealand national rugby team? ")
if question_2.lower() == "all blacks" :
    score = score + 1
    print("That is correct! Your current score is:", score)
else :
    print("That is incorrect! Your current score is:", score)

question_3 = input("How many stars does the New Zealand flag have? ")
if question_3.lower() == "4" or "four" :
    score = score + 1
    print("That is correct! Your current score is:", score)
else :
    print("That is incorrect! Your current score is:", score)

question_4 = input("New Zealand christmas is during what season? ")
if question_4.lower() == "summer" :
    score = score + 1
    print("That is correct! Your current score is:", score)
else :
    print("That is incorrect! Your current score is:", score)

question_5 = input("What is New Zealand's national animal? ")
if question_5.lower() == "kiwi" :
    score = score + 1
    print("That is correct! Your current score is:", score)
else :
    print("That is incorrect! Your current score is:", score)

print("You have completed the quiz! Your final score is:", score)
print("The time taken for you to complete it is:", datetime.today() - start_time)