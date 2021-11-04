# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

coupleName = name1 + name2
formattedNames = coupleName.lower()
tr00 = formattedNames.count("t")
tr01 = formattedNames.count("r")
tr02 = formattedNames.count("u")
tr03 = formattedNames.count("e")
trueComponent = tr00 + tr01 + tr02 + tr03

lv00 = formattedNames.count("l")
lv01 = formattedNames.count("o")
lv02 = formattedNames.count("v")
lv03 = formattedNames.count("e")
loveComponent = lv00 + lv01 + lv02 + lv03

loveCalc = int(str(trueComponent) + str(loveComponent))

if (loveCalc < 10) or (loveCalc > 90):
  print(f"Your score is {loveCalc}, you go together like coke and mentos.")
elif (loveCalc >= 40) and (loveCalc <= 50):
  print(f"Your score is {loveCalc}, you are alright together.")
else:
  print(f"Your score is {loveCalc}.")
