# Area of a circle

import math

pi = math.pi
def main():
    radius = float(input("Enter the radius of the circle: "))
    area = radius*radius*pi
    print(f"The area of the circle with radius {radius} is: {area:.2f}")
    
main()
