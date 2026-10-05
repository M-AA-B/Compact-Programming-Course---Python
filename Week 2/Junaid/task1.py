# Task 1 — Sort tuples by the last element

# Given list of tuples
my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Sort the list using the second element of each tuple
result = sorted(my_list, key=lambda x: x[1])

# Print the sorted list
print(result)