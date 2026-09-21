# a program that calculates the factorial of a number

zahl = int(input("Enter a number: "))

faktor = 1

for i in range(1, zahl + 1):
    faktor = faktor * i

print("The factorial is:", faktor)