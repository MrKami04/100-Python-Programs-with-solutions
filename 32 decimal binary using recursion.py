# progam that convert decimal into binary number.
print("😍 ------------------------- 😍")

number = int(input("enter the number:"))

def convertBianry(number):
    if number > 1:
        convertBianry(number // 2)
        
    print(number % 2, end="")

print("the binary of the given number is:")
convertBianry(number)
    
