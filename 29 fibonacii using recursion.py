# program that to display fibonacii sequence using recurion.
print("😍 ------------------------- 😍")

number  = int(input("enter the number:"))

def fibonacci(number):
    if number <= 1:
        return number
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)
if number <= 0:
    print("enter a positive number.")
else:
    print("Fibonacci sequence.")
    for i in range(number):
        print(fibonacci(i))