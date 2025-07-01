# program that check the given number is prime or not.
print("😀 -------------------- 😀")

number = int(input("Enter the number:"))

if number == 1:
    print("it is not a prime number.")
    
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(f"number {number} is not prime.")
            break
        
    else:
        print(f" number {number} is prime number🤣")
else:
    print(f"number {number} is not prime.😁")