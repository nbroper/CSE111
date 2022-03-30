#https://byui-cse.github.io/cse111-course/lesson09/prove.html
import csv
from datetime import datetime

KEY_INDEX = 0
NAME_INDEX = 1
PRICE_INDEX = 2

product_list = {}
request = {}
quantity_list = []
subtotal_list = []
tax_rate = 0.06

def main():
    """
    Calls the read_dict function and stores the compound dictionary in a 
    variable named products_dict.
    Prints the products_dict.
    Opens the request.csv file for reading.
    Contains a loop that reads and processes each row from the request.csv file. 
    Within the body of the loop, your program must do the following for each row:
    Use the requested product number to find the corresponding item in the products_dict.
    Print the product name, requested quantity, and product price.
    """
    try:
    
        #print name of the store
        print("Nate's Corner Store")
        
        #read file into a list
        read_dict("products.csv", KEY_INDEX)
            
            
        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)
            print(" ")
            for line in reader:
                key = line[0]
                quantity = line[1]
                products = list(product_list[key])
                print(f'{products[0]}: {quantity} @ {products[1]}')
        print(" ")

        get_totals()
        date()
    
    except FileNotFoundError as file_not_found_err:
        print("Error: missing file ")
        print("file_not_found_err")

    except KeyError as key_err:
        print("Error: unknown product ID in the request.csv file")
        print(type(key_err).__name__, key_err)

def read_dict(filename, KEY_COLUMN_INDEX):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        #skip first line of csv file
        next(reader)

        #for current row get product number, name, and price
        for row in reader:
            key = row[KEY_COLUMN_INDEX]
            product_list[key] = row
            product_list[key].pop(0)
            print(f'{key} {product_list}')
        
    return product_list

def get_totals():
    with open("request.csv", "rt") as request_file:
        reader = csv.reader(request_file)
        next(reader)
        for line in reader:
            quantity = int(line[1])
            quantity_list.append(quantity)
            
    #number of items
    total_items = (sum(quantity_list)) 
    print(f"Number of Items: {total_items} ")
    
    with open("request.csv", "rt") as request_file:
        reader = csv.reader(request_file)
        next(reader)
        for line in reader:
            key = line[0]
            quantity = float(line[1])
            products = list(product_list[key])
            subtotal = quantity * float(products[1])
            subtotal_list.append(subtotal)
            final_subtotal = sum(subtotal_list)
            tax = final_subtotal * tax_rate
            total = tax + final_subtotal

        #subtotal
        print(f"Subtotal: {subtotal} ")
        #sales tax
        print(f"Sales Tax: {tax:.2f}")
        #total
        print(f"Total: {total:.2f}")
        print(" ")
        print("Thanks for shopping at Nate's Corner Store. ")

def date():
    current_date_and_time = datetime.now()
    print(f"{current_date_and_time:%c} ")

if __name__ == "__main__":
    main()