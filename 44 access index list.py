# program that to access index of a list using for loop.
print("😍 ------------------------- 😍")

# method 1   ( by enumerate method)

list1 = [23, 45, 56, 78, 23,676]

for index , value in enumerate(list1, start=1):
    print(index, "-", value)


# method 2  ( for loop)
print("😍 ------------------------- 😍")
for index in range (len(list1)):
    value = list1[index]
    print(index, value)