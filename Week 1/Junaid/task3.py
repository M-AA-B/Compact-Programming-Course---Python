# a program that converts different data types and outputs the results

# 1. Convert an integer to a floating-point number
zahl = 10
kommazahl = float(zahl)
print("integer to a floating-point number", type(kommazahl))
print(kommazahl)


# 2. Convert a floating-point number to an integer.
kommazahl = 10.5
zahl = int(kommazahl)
print("float to int", type(zahl))
print(zahl)

# 3.Convert an integer to a string
zahl = 10
text = str(zahl)
print("integer to string conversion", type(text))
print(text)

# 4. Convert a string containing a number to an integer.
text = "10"
zahl = int(text)
print("string converted to int", type(zahl))
print(zahl)

# 5. Convert an integer to a Boolean

zahl = 10
booolean = bool(zahl)
print("int to bool conversion", type(booolean))
print(booolean)
