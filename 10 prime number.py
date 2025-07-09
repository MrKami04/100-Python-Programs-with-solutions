# program that check the given number is prime or not.
print("😀 -------------------- 😀")

number = int(input("Enter the number:"))

# if number == 1:
#     print("it is not a prime number.")
    
# if number > 1:
#     for i in range(2, number):
#         if number % i == 0:
#             print(f"number {number} is not prime.")
#             break
        
#     else:
#         print(f" number {number} is prime number🤣")
# else:
#     print(f"number {number} is not prime.😁")
    

print("😀 -------------------- 😀")


# print(f" number1 {number} is prime number🤣" if number > 1 and all(number % i != 0 for i in range(2, number)) else f"number {number} is not prime.😁")

# print(f" number2 {number} is prime number🤣" if number > 1 and not any(number % i != 0 for i in range(2, number)) else f"number {number} is not prime.😁")

print("😀 -------------------- 😀")
# # by function 
def prime_no(number):
    if number > 1:
        print("number is not prime" if any(number % i == 0 for i in range(2, number)) else "number is prime")
    else:
        print("number is not prime")
prime_no(number)

