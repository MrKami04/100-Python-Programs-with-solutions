# program that find the largest number from three given number.

print("😁-------------------😁")

number1 = int(input("Enter number1:"))
number2 = int(input("Enter number2:"))
number3 = int(input("Enter number3:"))

if number1 > number2 and number1  > number3:
    print(f"number1 {number1} is greatest number😎.")
    
elif number2 > number1 and number2 > number3:
    print(f"number2 {number2} is largest number🤗😀.")
    
else:
    print(f"number3 {number3} is greatest number😀😋😊.")
    
# by function

def largest():
    num1 = int(input("enter the number1 here:"))
    num2 = int(input("enter the number2 here:"))
    num3 = int(input("enter the number3 here:"))
    
    model = (num1, "is greatest") if (num1 > num2 and num1 > num3) else (num2, " is greatest") if (num2 > num1 and num2 > num3) else (num3, "is greatest")
    return model
print(f"by function {largest()}")
