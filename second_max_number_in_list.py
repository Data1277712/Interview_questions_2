def second_max_number(lst):
    # Sort the list
    lst.sort()
    # Remove duplicates by converting to a set and back to a list
    unique_lst = list(set(lst))
    # Sort the unique list
    unique_lst.sort()
    # Return the second last element
    return unique_lst[-2]

lst = [34, 43, 0, 89, -1, 89, 90, 90]
print(second_max_number(lst))  # Output: 89
