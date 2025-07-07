#  program that find square of number

print("----------------------------")

# method 1
number1 = int (input("Enter the number1 is : "))


square_root = number1**(1/2)
print(f"Square root of number2 is :{square_root} ")

print("----------------------------")
# method 2   (math module)

import math

number2 = int (input("Enter the number2 is : "))
squareroot = math.sqrt(number2)
print(f"Square root of number2 is : {squareroot}") 

print()
# function for find square root

def square_root():
    return math.sqrt(number2)
print(f"square root from function1 is {square_root()}")

# or 
def square_root(number2):
    sqr = number2**(1/2)
    return sqr
    
print(f"square root from function2 is {square_root(number2)}")