"""
v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.
"""


import math

tire_width = int(input('Enter the width of the tire in mm: '))
aspect_ratio = int(input('Enter the aspect ratio of the tire: '))
wheel_diameter = int(input('Enter the diameter of the wheel in inches: '))

volume = (math.pi * ((tire_width ** 2) * aspect_ratio) * ((tire_width * aspect_ratio) + (2540 * wheel_diameter))) / 10000000000

print(f"The approximate volume is {volume:.2f} liters. ")

