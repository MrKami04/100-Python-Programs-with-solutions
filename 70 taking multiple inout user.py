print("😍 --------------------------------- 😍")  
# simple method to take input from user

# a = input("enter a number here:")
# b = input("enter a number here:")
# c = input("enter a number here:")

# print("Yhe value of a is:",a)
# print("Yhe value of b is:",b)
# print("Yhe value of c is:",c)

print("😍 --------------------------------- 😍")  

# advance method to tka einput from user

# a,b,c = input("enter three value here").split()

# a,b,c = input("enter three value here:").split(",")

# print("Yhe value of a is:",a)
# print("Yhe value of b is:",b)
# print("Yhe value of c is:",c)

# print("The addition of the given numbers is: ")
# print((int(a)+int(b)+int(c)))


print("😍 --------------------------------- 😍")  

# lit comprehension method

a,b,c = [int(x) for x in input("enter three values:").split(",")]
print("The addition of the given numbers is: ")
print((int(a)+int(b)+int(c)))