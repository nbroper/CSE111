import csv
import numpy as np

with open('amazon_orders.csv', 'rt') as csv_file:      
    reader = csv.DictReader(csv_file)

    sub = []

    for row in reader:
        sub.append(row['Subtotal'])
        sub = list(map(lambda elem: elem.replace('$', ''), sub))
        #print(sub)
    float_sub = list(np.float_(sub))

    subtotal = sum(float_sub)
#print(sub)
print(f"Subtotal: {subtotal:.2f} ")

        
           
            


