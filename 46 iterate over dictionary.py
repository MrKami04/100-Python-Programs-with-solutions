# program that to iterate over dictionary using a for loop.
print("😍 ------------------------- 😍")

# method 1
dictionary1 = {"work":"hard","money":"enjoy","hot":"cold","go":"come"}
print(dictionary1)


for key, value in dictionary1.items():
    print(key,":", value)


# method 2  (key)
print("😍 ------------------------- 😍")
for key in dictionary1:
    print(key, ":", dictionary1[key])


# method 3  (key and value)

for key in dictionary1.keys():
    print(key)

for i in dictionary1.values():
    print(i)
