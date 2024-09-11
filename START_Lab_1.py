def lab1Question1(input_gb):
    # Convert the input of a number of gigabytes to the number of bytes
    num_bytes = 0
    # Do the work here
    # The solution to this goes here (and in all of them below...)
    # Set the variable num_bytes to the answer and return it
    num_bytes = input_gb * 1024 * 1024 * 1024
    return num_bytes

def lab1Question2(name):
    # Take an input of a name, return True if there is an odd number of characters in the name, False otherwise
    # Return None if the input is not a string
    is_odd = None
    if(type(name) != str):
        return is_odd
    if(len(name) % 2 == 0):
        is_odd = False
    else:
        is_odd = True
    return is_odd

def lab1Question3(input_string, input_number):
    # Take in two inputs - a string and a number
    # Return the character of the string in the index given by number.  If this index does not exist, then return -1.
    character_at = -1
    if(len(input_string) >= input_number):
        return input_string[input_number]
    else:
        return character_at

def lab1Question4(file_name):
    # Take an input of a file name. 
    # Read that file and return a list of all numbers in that file
    list_of_nums = []
    f=open(file_name, "r")
    for value in f.readlines():
        list_of_nums.append(value)
    return list_of_nums

def lab1Question5(list_numbers):
    # Take an input of a list of numbers
    # Return the mode from that list. 
    mode_of_list = None
    hVal = 0
    aDict={}
    for value in list_numbers:
        if value in aDict:
            aDict[value] += 1
        else:
            aDict[value] = 1 
    for key,value in aDict.items():
        if value > hVal:
            hVal = value
            mode_of_list = []
            mode_of_list.append(key)
        elif value == hVal:
            mode_of_list.append(key)
        else:
            continue
    return mode_of_list

def lab1Question6(quarters, dimes, nickels, pennies):
    # Take in 4 inputs - the number of quarters, dimes, nickels, and pennies in a handful
    # Return the total amount in dollars
    # For example, if the handful contains 4 quarters, 3 dimes, 2 nickels, and 1 penny, the function should return 1.41.
    total = None
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return total
 