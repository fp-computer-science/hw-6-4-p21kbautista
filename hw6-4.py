# Kyle Bautista (AMDG) 10/29/20

import calendar

# Question 1
print(calendar.TextCalendar().pryear(2020))

# Question 2
print(calendar.TextCalendar(firstweekday=6).pryear(2020))

# Question 3
print(calendar.TextCalendar().prmonth(themonth=1, theyear=2020))

# Question 4
print(calendar.LocaleTextCalendar(6, "ITALIAN").pryear(2020))
print(calendar.LocaleTextCalendar(6, "GERMAN").pryear(2020))
print(calendar.LocaleTextCalendar(6, "JAPANESE").pryear(2020))
print(calendar.LocaleTextCalendar(6, "CHINESE").pryear(2020))

# Question 5
print("The expected argument from 2020 would be True if its a leap year, false if its a non-leap year.")
print("The year 2020 is " + str(calendar.isleap(year=2020)))
print("This value is a True and False statement.")
