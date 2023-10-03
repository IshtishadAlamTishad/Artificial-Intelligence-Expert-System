import math
def c_area(r):
    area = math.pi * (r ** 2)
    return area


def c_perimeter(r):
    perimeter = 2 * math.pi * r
    return perimeter


r = float(input("Enter the radius: "))
circleArea = c_area(r)
circlePerimeter = c_perimeter(r)

print("Circle area is : ", circleArea)
print("Circle perimeter is:", circlePerimeter)