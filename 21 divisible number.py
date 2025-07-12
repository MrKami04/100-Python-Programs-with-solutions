# program that number divisible by another number.
print("😀 --------------------------------- .😆")

# method 1   ( by for loop )

print("the number divissible by 13 are:")

for i in range (1, 100):
    if i % 13 == 0:
        print(i)
    
    
# method 2  ( by lambda function and  filter ())
print("😀 --------------------------------- .😆")

number_list = [39, 48, 34, 26, 39, 33, 89, 98, 91]

result = list(filter(lambda x : x % 13 ==0,number_list))

print("the number divisible by 13 are:")
print(result)


print("😀 --------------------------------- .😆")
#  by function
def divisible_by_13(numbers):
    result = [x for x in numbers if x % 13 == 0]
    print("The numbers divisible by 13 are:")
    print(result)

number_list = [39, 48, 34, 26, 39, 33, 89, 98, 91]
divisible_by_13(number_list)
