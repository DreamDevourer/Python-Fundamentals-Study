"""
Interesting resources:
https://docs.python.org/3/library/functions.html#built-in-functions
https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals
https://docs.python.org/3/tutorial/introduction.html#numbers
https://docs.python.org/3/tutorial/modules.html#modules
"""

whatCurrency = input("What currency are you using? (USD/BRL) ")
incomePercentage = input("What is the income percentage per year? ")
investUntil = input("See the projection until: (ex: 5) ")
howMuch = input("How much do you want to invest? ")
print(" ")


# Calculate the income
FinalIncome = float(howMuch) * (float(incomePercentage) / 100)
totalIncome = float(FinalIncome) + float(howMuch)
print("Your final income in " + str(investUntil) +
      " years is " + str(totalIncome * int(investUntil)) + " " + whatCurrency)
print(" ")

# Print the income each year in investUntil
for eachYearIncome in range(1, int(investUntil) + 1):
    print("In " + str(eachYearIncome) + " year(s) you will have " +
          str(totalIncome * eachYearIncome) + " " + whatCurrency)
