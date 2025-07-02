# program that print the natural numbers.
print("😀 ------------------------------ 😀")

number = int(input("Enter the number:"))

if number < 0:
    print("please enter positive number.")
else:
    sum = 0
    while number > 0:
        sum += number
        number -= 1
        
    print(f"sum of natural numbers: {sum}")    
    