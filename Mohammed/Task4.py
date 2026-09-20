# Factorial of a number

def main():
    number = int(input("Enter a number: "))
    factorial = 1
    for n in range(1, number + 1):
        factorial *= n
    print(f"Factorial of {number} is {factorial}")
    
main()

