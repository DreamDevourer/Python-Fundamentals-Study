#Password Generator Project
import random
import secrets
import os
import sys


# Character Lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyMasterPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_randomOrder = input("Would you like your password to be in random order? (y/n)\n").lower()

#Easy Level - Order not randomized:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

def easyMode():
    def generateLetters():
        global letter
        letter = ""
        for lettersNum in range(nr_letters):
            letter += secrets.choice(letters)
        generateSymbols()


    def generateSymbols():
        global genSymbols
        genSymbols = ""
        for symbolNum in range(nr_symbols):
            genSymbols += secrets.choice(symbols)
        generateNumbers()

    def generateNumbers():
        global genNumbers
        genNumbers = ""
        for numNum in range(nr_numbers):
            genNumbers += secrets.choice(numbers)
        resultPassword()

    def resultPassword():
        print(f"Your password is: {letter}{genSymbols}{genNumbers}")
        # copy password to clipboard
        copyPass = letter+genSymbols+genNumbers
        os.system(f"echo {copyPass} | pbcopy")

    generateLetters()



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

passwdList = []


def hardMode():

    global passwdList

    def generateLettersH():
        global passwdList
        for lettersNum in range(nr_letters):
            passwdList += random.choice(letters)
        generateSymbolsH()

    def generateSymbolsH():
        global passwdList
        for symbolNum in range(nr_symbols):
            passwdList += random.choice(symbols)
        generateNumbersH()

    def generateNumbersH():
        global passwdList
        for numNum in range(nr_numbers):
            passwdList += random.choice(numbers)
        resultPasswordH()

    def resultPasswordH():
        global passwdList
        random.shuffle(passwdList)
        randomReadable = ""
        for eachChar in passwdList:
            randomReadable += eachChar

        print(f"Your random password is: {randomReadable}")
        # copy randomReadable to clipboard
        os.system(f"echo {randomReadable} | pbcopy")

    generateLettersH()

if nr_randomOrder == "y":
    hardMode()
else:
    easyMode()
