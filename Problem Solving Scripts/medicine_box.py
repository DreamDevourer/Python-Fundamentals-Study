"""
I need to take 1.6ml of a medicine every day. A box of this medicine comes with a bottle of 20ml.
"""
quantityTaken = 1.6
boxBottleQuantity = 20

monthsToTake = input("How many months do you need to take this medicine? ")
monthsToTake = int(monthsToTake)

print("Ok, you will take:",  quantityTaken * 30, " ml each month.")
print("So... You will have to take: ", (quantityTaken * 30)
      * monthsToTake, " ml of medicine in total.")
print("That means you will need to buy: ",
      int(((quantityTaken * 30) * monthsToTake) / boxBottleQuantity), " boxes of medicine.")
