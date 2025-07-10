# program that convert celsius temperature in fahrenheit.
print("😪 --------------------- 😫")

celsius = int(input("Enter temperature in celsius:"))

fahrenheit = (celsius) * (9/5) + 32

print(f"the converted value is {round(fahrenheit, 2)} Fahrenheit")


print("😪 --------------------- 😫")
# by function

def temper():
    return (celsius) * (9/5) + 32
print(f"temperature in fahrenhiete {round(temper(), 2)}")
