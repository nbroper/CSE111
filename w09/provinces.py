

def main():

    text_list = read_list("provinces.txt")

    #replace "AB" with "Alberta" in every occurance
    for i in range(len(text_list)):
        if text_list[i] == "AB":
            text_list[i] = "Alberta"
    
    #count how many times "Alberta" is in the list
    count = text_list.count("Alberta")

    print(text_list)
    print(count)

def read_list (filename):

    text_list = []

    with open(filename, "rt") as text_file:

        for line in text_file:

            clean_line = line.strip()

            text_list.append(clean_line)
      
    text_list.pop(0)
    text_list.pop()
    
        
    return text_list


if __name__ == "__main__":
    main()