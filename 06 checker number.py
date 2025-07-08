# program that check whether the number is positive or negative.
print("-------------------------------------")

number = int(input("😍 Enter the number:")) 

if number > 0:
    print("Number is positive.")

elif number < 0:
    print("number is negative")
    
else:
    print("Number is zero.🥰")
    
# by function

def no_checker():
   model =  "positive" if number > 0 else "negative" if number < 0  else "zero"
   return model

print(f"By function {no_checker()}")

