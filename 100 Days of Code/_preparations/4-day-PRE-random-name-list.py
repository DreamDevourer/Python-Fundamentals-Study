# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

randomName = random.choice(names)
print(f"The chosen one to pay the bill is: {randomName}.")
