# Task 2 — Sum and average of digits in a string

# Given string
s1 = "The number 5 is greater than 2"

# Create an empty list to store the digits
digits = []

# Go through each character in the string
for char in s1:

    # Check if the character is a digit
    if char.isdigit():

        # Convert the character into an integer and add it to the list
        digits.append(int(char))

# Calculate the sum of all digits
total = sum(digits)

# Calculate the average of the digits
average = total / len(digits)

# Print the results
print("Sum:", total)
print("Average:", average)