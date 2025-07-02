# program that find factors of the number
print("😀 --------------------------------- .😆")

number_variable = int(input("enter the number:"))

for i in range (1, number_variable + 1):
    if number_variable % i == 0:
        print(i)
