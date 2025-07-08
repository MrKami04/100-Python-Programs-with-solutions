# program that find the area of the triangle
print("---------------------------------------")
height = float(input("Enter the height of the triangle is:"))
base = float(input("Enter the base of the triangle is:"))

area = (0.5) * base * height

print(f"Area of triangle is : {area}")

# define function for find the area of triangle.

def triangle_area():
    area = (0.5) * base * height
    return area
print(f"area of triangle using function {triangle_area()}")

