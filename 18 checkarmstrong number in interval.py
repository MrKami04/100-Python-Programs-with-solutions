# program that find all armstrong number in given range.
print("😀 ---------------------------------- 😏")

lower_limit= int(input("Enter the lower_limit number:"))
upper_limit= int(input("Enter the upper_limit number:"))
print("Arnstrong numbers in given interval:")
for number in range (lower_limit, upper_limit + 1):
    length_variable = len(str(number))
    sum = 0
    temporary_variable = number

    while temporary_variable > 0:
        digit_variable = temporary_variable % 10
        sum += digit_variable ** length_variable
        temporary_variable //= 10
    if number  ==  sum:
        
        print(sum)