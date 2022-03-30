import csv
import numpy as np

KEY_INDEX = 1
ORDER_DATE_INDEX = 0
SUBTOTAL_INDEX = 13
SHIPPING_CHARGE_INDEX =14
TAX_CHARGED_INDEX = 17
TOTAL_CHARGED_INDEX = 18
order_list = []


def main():

    #read_dict("amazon_nodollar.csv", KEY_INDEX)
    
    # subtotal('amazon_orders.csv')
    # shipping('amazon_orders.csv')
    # tax('amazon_orders.csv')
    # promotion('amazon_orders.csv')
    # total('amazon_orders.csv')
    orders_per_year('amazon_orders.csv')    

def read_dict(filename, KEY_COLUMN_INDEX):
    """read the csv file into a compound dictionary and return the dictionary
    
    Parameters
        filename: the name of the csv file
        KEY_COLUMN_INDEX: the index of the column to use as the keys in the dictionary"""
    compound_dict = {}
    
    with open(filename, "rt") as csv_file:
        
        reader = csv.DictReader(csv_file)
        

        for row in reader:
            key = row[KEY_COLUMN_INDEX]

            compound_dict[key] = row
            order_date = row[0]
            subtotal = float(row[13])
            shipping = float(row[14])
            tax = float(row[17])
            total = float(row[18])
            print(f'{key} {order_date} {subtotal} {shipping} {tax} {total}')

    return compound_dict

def subtotal(filename):
    sub_list = []
    with open(filename, "rt") as csv_file:
        reader = csv.DictReader(csv_file)
        
        for row in reader:
            sub_list.append(row['Subtotal'])
            sub_list = list(map(lambda elem: elem.replace('$', ''), sub_list))
        float_sub = list(np.float_(sub_list))

    subtotal = sum(float_sub)
    print(f"Subtotal: ${subtotal:.2f}")


def shipping(filename):
    shipping_list = []
    with open(filename, "rt") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            shipping_list.append(row['Shipping Charge'])
            shipping_list = list(map(lambda elem: elem.replace('$', ''), shipping_list))
        float_ship = list(np.float_(shipping_list))
    
    shipping_cost = sum(float_ship)  
    print(f"Shipping: ${shipping_cost:.2f} ")
    
    
def tax(filename):
    tax_list = []
    with open(filename, "rt") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            tax_list.append(row['Tax Charged'])
            tax_list = list(map(lambda elem: elem.replace('$', ''), tax_list))
        float_tax = list(np.float_(tax_list))

    tax_charged = sum(float_tax)
    print(f"Tax Charged: ${tax_charged:.2f} ")

def promotion(filename):
    promo_list = []
    with open(filename, "rt") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            promo_list.append(row['Total Promotions'])
            promo_list = list(map(lambda elem: elem.replace('$', ''), promo_list))
        float_promo = list(np.float_(promo_list))

    promotions = sum(float_promo)
    print(f"Promotions Received (Discounts): ${promotions:.2f} ")

def total(filename):
    total_list = []
    with open(filename, "rt") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            total_list.append(row["Total Charged"])
            total_list = list(map(lambda elem: elem.replace('$', ''), total_list))
        float_total = list(np.float_(total_list))

    total = sum(float_total)
    print(f"Total Charged: ${total:.2f} ")

def orders_per_year(filename):
    order_year_list = []
    with open(filename, "rt") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader: 
            order_year_list.append(row["Order Date"])
            order_year_list = list(map(lambda elem: elem.replace("''/''P/", ''), order_year_list))
            print(order_year_list)
    
    
    
    
    
    
    # sub_total = (sum(dict))
    # print(f'{sub_total} ')

if __name__ == "__main__":
    main()