# program that mini_calculator
print("😀 --------------------------------- .😆")
print("  ")
print("___________ Mini Calculator ____________")

number1 = float(input("enter first numberc:"))
number2 = float(input("enter second number:"))

print(" press 1 for addition \n press 2 for substraction \n press 3 for multiplication \n pess 4 for division")

choice = int(input("enter your choice from 1 to 4:"))
if choice == 1:
    print(number1 + number2)
elif choice == 2:
    print(number1 - number2)
elif choice == 3:
    print(number1 * number2)
elif choice == 4:
    print(number1 / number2)
    
else:
    print("invalid input!")









