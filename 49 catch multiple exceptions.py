# program that to catch multiple exceptions in one line
print("😍 ------------------------- 😍")

string1 = input("enter the number here:")

try:
    number1 = int(input("enter the number here:"))
    print(number1 + string1)
    
except (ValueError, TypeError) as a:
    print(a)
    
print("Thank you!")