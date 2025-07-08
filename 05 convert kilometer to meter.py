# program that convert kilometer into meter
print("-----------------------------------")

kilometer = float(input("Enter the value in kilometer is : "))

miles = (0.621371) * kilometer

print(f"{kilometer} kms  will be: {miles} miles")


# by function
def km():
    miles = (0.621371)  *  kilometer
    return miles
print(km())
