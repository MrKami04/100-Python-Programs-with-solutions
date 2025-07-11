# prohram that print Armstrong number
print("😀 ---------------1------------ 😋")

# method 1  ( for three digit )
number = int(input("Enter the number:"))


length_variable = len(str(number))
result = 0
temporary_variable = number

if length_variable == 3:
    while temporary_variable > 0:
        digit_variable = temporary_variable % 10
        cube_variable = digit_variable ** 3
        result= result + cube_variable
        temporary_variable //= 10
    
    if result  == number:
        print('it is an armstrong number')

    else:
        print("it is not armstrong number.")
elif length_variable < 3:
    print("please enter the digit upto three or more as (153, 13411)")        
    

# method 2  ( for any number)
print("😀 ------------2--------------- 😋")


while temporary_variable > 0:
        digit_variable = temporary_variable % 10
        any_variable = digit_variable ** length_variable
        result = result + any_variable
        temporary_variable //= 10
    
if result  == number:
        print('it is an armstrong number')

else:
        print("it is not armstrong number.")


print("😀 ----------------3----------- 😋")
# by functions
def check_armstrong(number):
    length_variable = len(str(number))
    
    armstrong_sum = sum([int(digit) ** length_variable for digit in str(number)])
    
    if armstrong_sum == number:
        print('It is an Armstrong number')
    else:
        print('It is not an Armstrong number')

check_armstrong(number)






