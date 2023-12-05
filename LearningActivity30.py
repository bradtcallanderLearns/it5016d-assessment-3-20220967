# LearningActivity30.py
# Author: Brad Callander
# Date: 10/11/2023

# This learning activity is practice for using numeric operators.

import math

# Challenge 1
# Shape 1
side_j = int(input("Enter the length of side J:"))
side_k = int(input("Enter the length of side K:"))
print("The area of the shape is", side_j / 2 * side_k)

# Shape 2
side_q = int(input("Enter the length of side Q:"))
side_w = int(input("Enter the length of side W:"))
side_s = int(input("Enter the length of side S:"))
side_g = int(input("Enter the length of side G:"))
print("The area of the shape is", side_g * side_s - side_q * side_w)

# Shape 3
side_u = int(input("Enter the length of side U:"))
side_m = int(input("Enter the length of side M:"))
side_n = int(input("Enter the length of side N:"))
print("The area of the shape is", side_u * side_m + side_n / 2 * side_n)

# Challenge 2
# Shape 1
side_x = int(input("Enter the length of side X:"))
side_y = int(input("Enter the length of side Y:"))
print("The area of the shape is", side_x * side_y)

# Shape 2
side_x = int(input("Enter the radius of the circle:"))
print("The area of the shape is", side_x ** 2 * math.pi * 3/4)

# Shape 3
side_g = int(input("Enter the length of side G:"))
side_e = int(input("Enter the length of side E:"))
side_f = int(input("Enter the length of side F:"))
print("The area of the shape is", side_f / 2 * side_g + side_e * side_g + (side_g/2) ** 2 * math.pi/2)

# Challenge 3
# Shape 1
side_e = int(input("Enter the length of side E:"))
side_d = int(input("Enter the length of side D:"))
print("The area of the shape is", side_d / 2 * math.sqrt(side_e ** 2 - side_d ** 2))

# Shape 2
side_f = int(input("Enter the length of side F:"))
print("The area of the shape is", side_f / 2 * side_f * math.cos(math.radians(40)))

# Shape 3
side_g = int(input("Enter the length of side G:"))
side_e = int(input("Enter the length of side E:"))
side_new = side_g / math.cos(math.radians(38))
print("The area of the shape is", side_new / 2 * side_g + side_e * side_g + (side_g / 2) ** 2 * math.pi / 2)