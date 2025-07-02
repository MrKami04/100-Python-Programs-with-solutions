# program that print the fibonacci sequence upto interval.
print("😀 --------------------------- 😋")

variable1 = 0
variable2 = 1

number = int(input("Enter the number 😎:"))

if number == 1:
    print(variable1)
else:
    print(variable1)
    print(variable2)
    for i in range (2, number):
        variable3 = variable1 + variable2
        variable1 = variable2
        variable2 = variable3
        print(variable3)