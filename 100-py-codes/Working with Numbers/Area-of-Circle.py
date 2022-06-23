## To calculate the Area of a circle

## Formula : pi*r*r

## Using Radius

from cmath import pi

radius = int(input("Enter the radius of a circle: "))
area = pi*radius*radius
print("The area of circle is:", (area))



## Using Diameter
## Formula: area = (pi*d*d)/4

from math import pi
diameter = int(input("Enter diameter: "))
area = (pi*diameter*diameter)/4
print("The area of circle is:", area)