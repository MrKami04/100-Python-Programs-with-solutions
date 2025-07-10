# program that print prime number in a given interval
print("😀 -------------------------- 😀")

lower_limit = 0
upper_limit = 50

for number in range (lower_limit , upper_limit + 1):
    if number > 1:
        
        for i in range(2, number):
            if number % i == 0:
                break
            
        else:
            print(f"number {number} is prime number")
            
            

print("😀 -------------------------- 😀")
prime_numbers = [number for number in range(lower_limit, upper_limit + 1)
                 if number > 1 and all(number % i != 0 for i in range(2, number))]

for number in prime_numbers:
    print(f"number {number} is prime number")
