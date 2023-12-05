# LearningActivity35.py
# Author: Brad Callander
# Date: 13/11/2023

# This learning activity is practice for using if elif statements.

# Challenge 1
print("Earthquake richter scale")
magnitude = float(input("Enter the earthquake magnitude: "))
print("The magnitude for this earthquake is:", magnitude)
if magnitude >= 10.0 :
    print("The earthquake is classed as Meteoric!")
elif magnitude >= 8.0 :
    print("The earthquake is classed as Great!")
elif magnitude >= 7.0 :
    print("The earthquake is classed as Major!")
elif magnitude >= 6.0 :
    print("The earthquake is classed as Strong!")
elif magnitude >= 5.0 :
    print("The earthquake is classed as Moderate.")
elif magnitude >= 4.0 :
    print("The earthquake is classed as Light.")
elif magnitude >= 3.0 :
    print("The earthquake is classed as Minor.")
elif magnitude >= 2.0 :
    print("The earthquake is classed as Very Minor.")
else :
    print("The earthquake is classed as Micro.")