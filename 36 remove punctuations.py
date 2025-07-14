# program that remove the punctuations in the string
print("😍 ------------------------- 😍")

punctuation_variable = """!()-[]{};:'",<>./?@#$%^&*)~"""

string_variable = input("enter the string: ")
empty_string = ""

for i in string_variable:
    if i not in punctuation_variable:
        empty_string += i

print(empty_string)


# by comprehension

empty_string = "".join([i for i in string_variable if i not in punctuation_variable])
print(empty_string)
