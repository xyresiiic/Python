# Program to find the volume of different shapes
import math

def volume_of_cube(side):
    # Volume of a cube = side^3
    return side ** 3

def volume_of_cylinder(radius, height):
    # Volume of a cylinder = pi * r^2 * h
    return math.pi * (radius ** 2) * height

print("--- Volume Calculator ---")

# 1. Cube
cube_side = 5
print(f"Volume of a cube with side {cube_side}: {volume_of_cube(cube_side):.2f}")

# 2. Cylinder
cyl_radius = 3
cyl_height = 10
print(f"Volume of a cylinder with radius {cyl_radius} and height {cyl_height}: {volume_of_cylinder(cyl_radius, cyl_height):.2f}")

