# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

ageLimit = 100 - int(age)

days = 365
weeks = 52
months = 12

daysUntilLimit = round(days * ageLimit)
weeksUntilLimit = round(weeks * ageLimit)
monthsUntilLimit = round(months * ageLimit)

print(f"You have {daysUntilLimit} days, {weeksUntilLimit} weeks, and {monthsUntilLimit} months left until 100 years.")
