# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

randomLen = len(names)
randomIndex = random.randint(0, randomLen - 1)
print(names[randomIndex])
