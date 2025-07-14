# program that to find the su of natural number using recursion.
print("😍 ------------------------- 😍")

number = int(input("enter the number upto sum :"))
def natural_number_sum(number):
    if number <= 1:
        return number
    else:
        return (number) + natural_number_sum(number - 1)
if number <= 0:
    print("enter a positive number.")
else:
    print("sum of natural number upto given number is:", natural_number_sum(number)) 
