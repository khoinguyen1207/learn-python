from numpy import array

# List comprehension is a concise way to create lists in Python.
lst = [1, 2, 3, 4, 5]
new_lst = [item for item in lst if item % 2 == 0]
new_lst_2 = [item if item % 2 == 0 else item + 2 for item in lst]
print(new_lst)  # Output: [2, 4]
print(new_lst_2)  # Output: [3, 2, 5, 4, 7]

# List comprehension can also be used to create dictionaries and sets.
# Dictionary comprehension
lst_2 = [1, 2, 3, 4, 5]
new_dict = {f"id_{item}": item + 2 for item in lst_2}
print(new_dict)  # Output: {1: 3, 2: 4, 3: 5, 4: 6, 5: 7}

# Set comprehension
lst_3 = [1, 2, 3, 4, 5, 5, 2, 7]
new_set = {item for item in lst_3}
print(new_set)  # Output: {1, 2, 3, 4, 5, 7}

array_1 = array([1, 2, 3, 4, 5])
