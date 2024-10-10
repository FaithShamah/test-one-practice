#Question_2(a)
import math
#Using a function,create a program that calculates the volume of a cylinder.V=pie*r**2h
radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))
pie_value = math.pi
volume = pie_value * radius**2 *height
print(f"the volume of the cylinder with radius {radius} and height {height} is {volume:.2f}")