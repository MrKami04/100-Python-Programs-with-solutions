# program that display power of 2 using anpnymous function
print("😀 ------------------------------- 😀")

n_terms  = int(input("Enter number of terms here:"))

result = list(map(lambda x : 2 ** x , range(n_terms + 1)))

print(result)

for i in range (n_terms + 1):
    print("the value of 2 raised to power", i , "is", result[i])