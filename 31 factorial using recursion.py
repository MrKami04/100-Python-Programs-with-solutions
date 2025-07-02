# program that find factorial using the recursio .
print("😍 ------------------------- 😍")

number = int(input("enter the number:"))

def factorial(number):
    if number == 1:
        return number
    else:
        return (number * factorial(number - 1))
    
if number <= 0:
    print('Factorial of number less then 1 does not exist.')
else:
    print("Factorialof given number is :", factorial(number))