# programthat to convert string to datetime.
print("😍 ------------------------- 😍")

# method 1   (by datetime module)

from datetime import datetime
date = "Oct 14 1997 7:15AM"

datetime1 = datetime.strptime(date, "%b %d %Y %I:%M%p")
print(datetime1)
print(type(datetime1))

# method 2  (dateutil Module)
print("😍 ------------------------- 😍")
from dateutil import parser

datetime1 = parser.parse("Oct 14 1997 7:15AM")
print(datetime1)
print(type(datetime1))