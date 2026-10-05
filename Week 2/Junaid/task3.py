# Task 3 — Sort a list of dictionaries using Lambda

# Given list of dictionaries
cars = [
    {'make': ' Google ', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

# Sort the dictionaries according to the 'make' value
result = sorted(cars, key=lambda x: x['make'])

# Print the sorted list
print(result)