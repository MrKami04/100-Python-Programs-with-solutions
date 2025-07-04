# progam that iterator along with next function.
print("😍 ------------------------- 😍")

# method for numbers
number_list  = [ 1,2,3,4,5,6,7,8]
iterate_variable = iter(number_list)
print(iterate_variable.__next__())
print(iterate_variable.__next__())
print(iterate_variable.__next__())


# method for string
print("😍 ------------------------- 😍")
string_1 = "hi hello how are you."
# for i in string_1:
#     print(i)
iterate_variable = iter(string_1)
# print(iterate_variable.__next__())
# print(iterate_variable.__next__())
print(iterate_variable.__next__())
# print(iterate_variable.__next__())
print(next(iterate_variable))



# we can create our iterator as 
print("😍 ------------------------- 😍")

class fantastic_number:
    def __init__(self):
        self.number_variable = 1
        
        
    def __iter__(self):
      return self

    def __next__(self):
       if self.number_variable <= 5:
           value_variable = self.number_variable
           self.number_variable+= 1
           return value_variable
       else:
            raise StopIteration
    
FN = fantastic_number()

for i in FN:
   print(i)

