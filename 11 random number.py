# program that generate random number.
print("😀 ---------------------------😀")

import random

number = random.randint(0 , 50)

print(f" random number is : {number}")


# Find first 10 triangular numbers
def triangular_numbers(n):
    for i in range(1, n + 1):
        t_num = i * (i + 1) // 2
        print(f"Triangular number {i} is {t_num}")

triangular_numbers(20)
