# prohram that print Armstrong number
print("😀 --------------------------- 😋")

# method 1  ( for three digit )
number = int(input("Enter the number:"))


length_variable = len(str(number))
sum = 0
temporary_variable = number

if length_variable == 3:
    while temporary_variable > 0:
        digit_variable = temporary_variable % 10
        cube_variable = digit_variable ** 3
        sum = sum + cube_variable
        temporary_variable //= 10
    
    if sum  == number:
        print('it is an armstrong number')

    else:
        print("it is not armstrong number.")
elif length_variable < 3:
    print("please enter the digit upto three or more as (153, 13411)")        
    
else:   
# method 2  ( for any number)
    print("😀 --------------------------- 😋")


    while temporary_variable > 0:
        digit_variable = temporary_variable % 10
        any_variable = digit_variable ** length_variable
        sum = sum + any_variable
        temporary_variable //= 10
    
    if sum  == number:
        print('it is an armstrong number')

    else:
        print("it is not armstrong number.")


