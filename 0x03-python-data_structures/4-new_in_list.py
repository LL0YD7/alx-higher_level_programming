def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):  # Check if idx is negative or out of range
        return my_list[:]  # Return a copy of the original list using list slicing
    else:
        new_list = my_list[:]  # Create a copy of the original list
        new_list[idx] = element  # Replace the element at the specified index with the new element
        return new_list  # Return the modified list

