# program that display calender
print("😍 ------------------------- 😍")

import calendar

year = int(input("enter the year:"))
month = int(input("enter the month:"))

calendar = calendar.month(year, month)
print(calendar)

# comprehension code
print("😍 ------------------------- 😍")
import calendar


[print(line) for line in calendar.month(year, month).split('\n')]
