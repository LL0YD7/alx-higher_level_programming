def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list) - 1, -1, -1):  # Iterate over the list in reverse order
        print("{:d}".format(my_list[i]))  # Print each integer using str.format() with integer format specifier

