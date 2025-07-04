# program that list comprehension (comprehension that mean single line of code)
print("😍 ------------------------- 😍")
list_1 = ["iterator","stero","hello","hi"]
# simple method
# for i in list_1:
#     print(i.upper)

# comprehension method
new_list = [i.upper() for i in list_1]
print(new_list)


# more about code

list_2 = [i for i in range(10)]
print(list_2)


# simple code 
new_list1 = []
list_3 = [1,2,3,4,5,6,7,8]
for i in list_3:
    if i % 2 == 0:
        new_list1.append(i)
print(new_list1)

# comprehension code
list_4 = [i for i in range(10) if i % 2 == 0] 
print(list_4)