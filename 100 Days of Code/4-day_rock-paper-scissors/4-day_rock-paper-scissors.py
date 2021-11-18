import random
import sys
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

visualSet = {"Rock": rock, "Paper": paper, "Scissors": scissors}
aiChoice = random.choice(list(visualSet.values()))

print("Welcome to the game.\n0 - Rock\n1 - Paper\n2 - Scissors")
userSet = input("Type a number: \n")

if userSet == "0":
    selectedHuman = visualSet["Rock"]
    print(f"HUMAN:\n{selectedHuman}")
    print(f"AI:\n{aiChoice}")
    if aiChoice == paper:
        print("AI wins")
    elif aiChoice == rock:
        print("Tie")
    elif aiChoice == scissors:
        print("Human wins")

elif userSet == "1":
    selectedHuman = visualSet["Paper"]
    print(f"HUMAN:\n{selectedHuman}")
    print(f"AI:\n{aiChoice}")
    if aiChoice == paper:
        print("Tie")
    elif aiChoice == rock:
        print("Human wins")
    elif aiChoice == scissors:
        print("AI wins")

elif userSet == "2":
    selectedHuman = visualSet["Scissors"]
    print(f"HUMAN:\n{selectedHuman}")
    print(f"AI:\n{aiChoice}")
    if aiChoice == paper:
        print("Human wins")
    elif aiChoice == rock:
        print("AI wins")
    elif aiChoice == scissors:
        print("Tie")

else:
    print("Invalid input")
    sys.exit(-1)
