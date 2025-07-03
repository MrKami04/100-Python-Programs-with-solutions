# program that to concatenate two lists
print("😍 ------------------------- 😍")

# method 1    ( by plus operator)
list1 = [2,3,4,5,6,7, "aa","ss",'pp']
list2 = [8,9,70,44,"ff","rr"]

list12 = list1 + list2
print(list12)

print("😍 ------------------------- 😍")

# method 2   (with unique values)

list13 = list(set(list1 +list2))
print(list13)

print("😍 ------------------------- 😍")

# method 3  (extend() function)

list14 = list1.extend(list2)
print(list14)