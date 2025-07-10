# program that print multiplication table  any number.
print("😀 --------------------------- 😋")

# method 01
number = int(input("Enter the number:"))

for i in range (1, 11):
    print(f"{number} X {i} = {number * i}")
    
    
# method 2
print("😀 --------------------------- 😋")
variable_1 = 1
while  variable_1 <= 10:
    print(number , "X" , variable_1 , "=" , number * variable_1)
    variable_1 = variable_1 + 1
    
    
# by function 
print("😀 --------------------------- 😋")

table = [f"{number} X {i} = {number * i}" for i in range(1, 11)]
for line in table:
    print(line)
