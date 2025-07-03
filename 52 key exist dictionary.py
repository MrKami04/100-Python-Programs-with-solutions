# program that to check if a key is already present in dictionary
print("😍 ------------------------- 😍")


marks_dictionary = {'jonh':23,"kalo":54,"lisa":22, "sido":98,"kilop":88}


name = input("enter the name here:")
if name in marks_dictionary.keys():
    print("it is present.")
    
else:
    print("not present")
