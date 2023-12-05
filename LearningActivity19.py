# LearningActivity19.py
# Author: Brad Callander
# Date: 09/11/2023

# This learning activity is practice for using boolean types.

import random

# Challenge 1
male = False
male = bool(random.randint(0, 1))
if(male):
    print("We will name the baby Rangi")
else:
    print("We will name the baby Anahera")
print(bool(True))

# Challenge 2
print("Test 1", bool(True))
print("Test 2", bool(False))
print("Test 3", bool("text"))
print("Test 4", bool(""))
print("Test 5", bool(" "))
print("Test 6", bool(0))
print("Test 7", bool())
print("Test 8", bool(3))
print("Test 9", bool(None))