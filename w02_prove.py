
from datetime import datetime
current_date_and_time = datetime.now()

import math

tire_width = int(input('Enter the width of the tire in mm: '))
aspect_ratio = int(input('Enter the aspect ratio of the tire: '))
wheel_diameter = int(input('Enter the diameter of the wheel in inches: '))

volume = (math.pi * ((tire_width ** 2) * aspect_ratio) * ((tire_width * aspect_ratio) + (2540 * wheel_diameter))) / 10000000000

print(f"The approximate volume is {volume:.2f} liters. ")

with open("volumes.txt", "at") as volumes_file:
    print(f"{current_date_and_time:%Y-%m-%d}, {tire_width}, {aspect_ratio}, {wheel_diameter}, {volume:.2f}", file=volumes_file)
