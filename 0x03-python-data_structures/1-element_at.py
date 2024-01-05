def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):  # Check if idx is negative or out of range
        return None  # Return None if idx is negative or out of range
    else:
        return my_list[idx]  # Return the element at the specified index
