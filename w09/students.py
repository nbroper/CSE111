import csv


def main():

    I_NUM_INDEX = 0
    NAME_INDEX = 1

    students_dict = read_dict("students.csv", I_NUM_INDEX)

    search = input("Please enter an I-Number (xxxxxxxxx):  ")

    if search not in students_dict:
        print("No such student")

    else: 
        value = students_dict[search]
        name = value[NAME_INDEX]

        print(name)

def read_dict(filename, KEY_COLUMN_INDEX):

    dictionary = {}

    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:

            key = row_list[KEY_COLUMN_INDEX]

            dictionary[key] = row_list
            
    return dictionary 
         
if __name__ == "__main__":
    main()

    

    