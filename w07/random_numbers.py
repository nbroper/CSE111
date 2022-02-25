import random 

def main():
    
    #create the initial number list and print it
    numbers = [1.76, 6.4, 38.6]
    print(numbers)
    #call append_random_numbers once, add number to list and print it
    append_random_numbers(numbers, 1)
    print(numbers)
    #call append_random_numbers three times, add numbers to list and print them
    append_random_numbers(numbers, 3)
    print(numbers)


def append_random_numbers(numbers_list, quantity=1):

    """
    generate the random number between 1 and 40, 
    round it to 2 spots after the decimal
    append it to the numbers list under main()
    """
    for i in range(quantity):
        
        numbers_list.append(round(random.uniform(1, 40), 1))
    
if __name__ == "__main__":
    main()