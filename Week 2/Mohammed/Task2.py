
def main():
    s1 = input("Enter a string: ")
    sum = 0
    count = 0
    for n in s1:
        if n.isdigit():
            count += 1
            sum += int(n)
            
    print(f" sum of digits in {s1} is {sum}")
    print(f" average of digits in {s1} is {sum/count}")
main()

