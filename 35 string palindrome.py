# program that to check whether a string os palindrome or not.
print("😍 ------------------------- 😍")

string_variable = input("enter the word here:")

reverse_variable = string_variable[::-1]

if string_variable == reverse_variable:
    print("it is  palindrome string.")
else:
    print(" it is not palindrome.")



# by comprehension
print("it is a palindrome string." if (string_variable := input("Enter a string: ")) == string_variable[::-1] else "it is not palindrome.")

