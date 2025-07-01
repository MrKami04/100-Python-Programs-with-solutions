# program that check thee year is leap or not.
print("🤩-------------------------😍")

# not leap year = 365 days
# leap year = 366 days
# conditions for leap year is : 1. leapyear % 400 == 0 , leapyear % 100 == 0
# 2. leapyear % 4 == 0 , leapyear % 100 == 0 

year = int(input("Enter the year❤❤:"))

if ( year % 400 == 0) and (year % 100 == 0):
    print(year, " is a leap year")
elif (year % 4 == 0) and (year % 100 != 0):
    print(year, "is a leap year.")
else:
    print(year, " is not a leap year.") 

