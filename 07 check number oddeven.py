# program that number is odd or even.
print("🤩-------------------------😍")

number = float(input("Enter the number:"))

if number % 2 == 0:
    print("Number is even😘.")
    
else:
    print("Number is odd😂.")    
    
    
# by function

def odd_no():
    return  "number is even" if number % 2 == 0 else "number is odd"
print(f"by function {odd_no()}")