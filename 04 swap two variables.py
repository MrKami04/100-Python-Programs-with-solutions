# program that swap thwo variable
print("-------------------------------")
# method 1   ( with help of temporary variable)

variable1 = 10
variable2 = 30

temporary_variable = variable1

print("The value of temporary-bariable is : ", temporary_variable )

variable1 = variable2
print(f"the value of variable1 is:", variable1)

variable2 = temporary_variable 
print(f"the value of variable2 is:", variable2)


# method 2  (without temporary variable)
print("----------------------------------")

variable_1 = 12
variable_2 = 13

variable_1 , variable_2 = variable_2 , variable_1

print(f"the value of variable_1 is :{variable_1}")
print(f"the value of variable_2 is :{variable_2}")

# by function
def swap(var_1, var_2):
    var_1 , var_2 = var_2, var_1
    return var_1, var_2

after = swap(12,34)

print(after)

