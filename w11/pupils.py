import csv
from unittest.util import sorted_list_difference


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    
        students_list = read_compound_list("pupils.csv")
        print(students_list)


        sorted_list_1 = sort_oldest_to_youngest(students_list)
        print("Ordered from Oldest to Youngest")
        print_list(sorted_list_1)

        sorted_list_2 = sort_by_given_name(students_list)
        print("Ordered by Given Name")
        print_list(sorted_list_2)
        
        
        
        #call to the sorted function that will sort students_list by birthdate 
        #from oldest to youngest
        

        #print the students_list by calling the print_list function

def sort_oldest_to_youngest(students_list):
    #lambda function that extracts students birthdate
    pull_birthdate = lambda student: student[BIRTHDATE_INDEX]
    print("")

    #call sorted function to sort the list of students
    sorted_list = sorted(students_list, key=pull_birthdate)
    return sorted_list

def sort_by_given_name(students_list):
    pull_name = lambda student: student[GIVEN_NAME_INDEX]
    print("")
    
    sorted_list = sorted(students_list, key=pull_name)
    return sorted_list

def sort_by_birth_month_and_day(students_list):
    def extract_month_and_day(student):
        birthdate_string = student(BIRTHDATE_INDEX)
        month_and_day = birthdate_string[5:]
        return month_and_day
        
    sorted_list = sorted(students_list, key=extract_month_and_day)

    return sorted_list

def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(compound_list):
    #function should include a for loop that prints each element on a separate line.

    for element in compound_list:
            print(element)
    print()

if __name__ == "__main__":
    main()