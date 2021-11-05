#Password Generator Project
import random
import secrets

# Character Lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyMasterPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

def generateLetters():
    global letter
    for lettersNum in range(nr_letters):
        letter = secrets.choice(letters)
        print(letter, end="")
    generateNumbers()

def generateNumbers():
    global genNumbers
    for numNum in range(nr_numbers):
        genNumbers = secrets.choice(numbers)
        print(genNumbers, end="")
    generateSymbols()

def generateSymbols():
    global genSymbols
    for symbolNum in range(nr_symbols):
        genSymbols = secrets.choice(symbols)
        print(genSymbols, end="")
    print(genSymbols)


generateLetters()
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
