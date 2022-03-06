import csv

PRODUCT_NUM_INDEX = 0
QUANTITY_INDEX = 1


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
    
    PRODUCT_NUM_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2
    
    products_dict = read_dict("products.csv", PRODUCT_NUM_INDEX)

    print(f"Products {products_dict} ")

    #read file into a list
    with open("request.csv", "rt") as request_file:

        reader = csv.reader(request_file)
        next(reader)

        for row_list in reader:

            product = row_list[PRODUCT_NUM_INDEX]
            quantity = int(row_list[QUANTITY_INDEX])
            #price = float(row_list[PRICE_INDEX])
            product = row_list
            

            print(product, quantity)
     


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
    dictionary = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        #skip first line of csv file
        next(reader)

        #for current row get product number, name, and price
        for row in reader:

            product_number = row[KEY_COLUMN_INDEX] 
            name = row[1]
            price = float(row[2])
            
            #store the data in the dictionary
            dictionary[product_number] = [name, price]


            # key = row_list[KEY_COLUMN_INDEX]
            # dictionary[key] = row_list

    return dictionary

if __name__ == "__main__":
    main()