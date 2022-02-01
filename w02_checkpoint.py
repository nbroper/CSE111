#python boxes.py

from re import match
from typing import Match


import math


items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

#boxes = items / items_per_box
#boxes_needed = math.ceil(boxes)

boxes_needed = math.ceil(items / items_per_box)

print(f"For {items} items, packing {items_per_box} items in each box, you will need {boxes_needed} boxes. ")