# program that sort words in alphabetically order.
print("😍 ------------------------- 😍")

string_variable = input("enter the string here:")

comma_separat_variable = string_variable.split()
print(f"This is  comma separated values {comma_separat_variable}")

for i in range(len(comma_separat_variable)):
    comma_separat_variable[i] = comma_separat_variable[i].lower()
print(f"This is lower case {comma_separat_variable}")

comma_separat_variable.sort()
print(f"This is sorted values in alphabetically order {comma_separat_variable}")




#  by comprehenion
print("😍 ------------------------- 😍")

comma_separat_variable = sorted([word.lower() for word in string_variable.split()])
print(f"This is sorted values in alphabetically order {comma_separat_variable}")
