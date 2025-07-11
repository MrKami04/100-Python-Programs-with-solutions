# program that print the natural numbers.
print("😀 ------------------------------ 😀")

number = int(input("Enter the number:"))

if number < 0:
    print("please enter positive number.")
else:
    result = 0
    while number > 0:
        result += number
        number -= 1
        
    print(f"sum of natural numbers: {result}")    
    

print("😀 ------------------------------ 😀")
# By function
def sum_natural_numbers(number1):
    result = sum([i for i in range(1, number1 + 1)]) if number1 > 0 else 0
    print(f"sum of natural numbers: {result}")
    
    if number <= 0:
        print("please enter a positive number greater than 0.")

number1 = int(input("Enter a number: "))
sum_natural_numbers(number1)


