# program tht how to check if a string is a valid keyword in python.
print("😍 ------------------------- 😍")

import keyword

words = [ "break","hello","lambda","continue","hole"]

for i in range (len(words)):
    if keyword.iskeyword(words[i]):
        print((words[i], "is a keyword in python."))
    else:
        print(words[i],"is not a keyword in python.")


print("😍 ------------------------- 😍")

print(f"if you want to check all keyword in python then this is keywords in python: \n\n {keyword.kwlist}")