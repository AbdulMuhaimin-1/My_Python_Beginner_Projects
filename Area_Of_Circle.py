from math import pi
def area(radius):
    Area = pi*radius**2
    return Area

Radius = float(input("Enter radius to calculate area: "))
print(f"The area is: {area(Radius)}")
