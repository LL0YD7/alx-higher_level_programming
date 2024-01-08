#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):  # Check if idx is negative or out of range
        return my_list  # Return the original list if idx is negative or out of range
    else:
        my_list[idx] = element  # Replace the element at the specified index with the new element
        return my_list  # Return the modified list
