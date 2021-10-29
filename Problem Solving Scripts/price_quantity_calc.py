"""
Idea:
A fair sells hot dog and refrigerant.
Each hot dog is sold by 8 USD.
Each refrigerant is sold by 5 USD.
"""

howManyHD = input("How many hot dogs do you want to buy? ")
howManyRef = input("How many refrigerants do you want to buy? ")

#Values in USD
hotDogPrice = 8.0
refPrice = 5.0

finalHDInt = int(howManyHD)
finalRefInt = int(howManyRef)

print("You have to pay: $", (finalHDInt * hotDogPrice) + (finalRefInt * refPrice))
print("Thank you.")
