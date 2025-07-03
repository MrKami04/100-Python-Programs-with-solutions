# program that check list is emptyor not.
print("😍 ------------------------- 😍")


# method 1   (by boolean)
empty_list = []
if not empty_list:
    print("the list is empty")

print("😍 ------------------------- 😍")
# method 2    (by len(function))
if len(empty_list) == 0:
    print("the list is empty")
    
print("😍 ------------------------- 😍")
# method 3    ([])

if empty_list == []:
    print("the list is empty")