# program that count the vowel in the string.
print("😍 ------------------------- 😍")

# method 1      (using dictionary)
variable1 = "Herry Potter and the prisoner of azkaban"

vowels = "aeiou"

variable1 = variable1.casefold()    # convert all capital letters into small 

count_variable = {}. fromkeys(vowels,0)

for char in variable1:
    if char in count_variable:
        count_variable[char]+= 1
        
print(count_variable)


# method 2           (list comprehension)


count_variable1 = {key:sum([1 for char in variable1 if char == key])for key in vowels}

print(count_variable1)