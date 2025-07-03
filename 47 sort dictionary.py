# program to sort a dictionary by value.
print("😍 ------------------------- 😍")

marks_dictionary = {'jonh':23,"kalo":54,"lisa":22, "sido":98,"kilop":88}
print(marks_dictionary)
# method 1  ( base on value)

sort_dictionary = sorted(marks_dictionary.items(), key = lambda x : x[1])
print(sort_dictionary)

# method 2
print("😍 ------------------------- 😍")
sort_value = sorted(marks_dictionary.values())
print(sort_value) 
