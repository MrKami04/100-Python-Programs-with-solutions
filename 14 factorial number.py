
# # program that find factorial of the given number.
print("🤑 -------------------------- 🤑")

# # method 1  ( by for loop)
number = int(input("Enter the number:"))
factorial = 1
if number < 0:
    print("factorial does not exit.")
    
if number == 0: 
    print("factorial is : 1")
if number > 0:
    for i in range (1, number + 1):
        factorial = factorial * i
    
print("Factorial ( by for loop method) of the given number is :", factorial)
    

# # method 2  ( by recursion)
print("🤑 -------------------------- 🤑")
# Recursion: call function in function this is called recursion
def factorial_1(number):
    if number == 0:
        return 1
    
    elif number < 0:
        return "Factorial does not exist."
    
    else:
        return ((number) * factorial_1 (number - 1))
    
result = factorial_1(number)
print("Factorial (by function method) of the number is:", result)

print("🤑 -------------------------- 🤑")
# as we write 

from math import prod

factorial = prod(range(1, number+1))
print(f"factorial of given number :{factorial}")