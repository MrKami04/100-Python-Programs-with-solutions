# program that find  HCF OR GCD 
print("😀 --------------------------------- .😆")

def find_hcf(variable_x, variable_y):
    if variable_x > variable_y:
        smaller = variable_y
    else:
        smaller = variable_x
        
    for i in range ( 1, smaller + 1):
        if ((variable_x % i == 0) and (variable_y % i == 0)):
            hcf = i
    return hcf 

print("the HCF of the given two numbers is :", find_hcf(12,30))


# comprehension method

def find_hcf(x, y):
    return max([i for i in range(1, min(x, y) + 1) if x % i == 0 and y % i == 0])

print("The HCF of the given two numbers is:", find_hcf(12, 30))
