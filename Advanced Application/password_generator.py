import random

# Variables
lowerCase = "abcdefghijklmnopqrstuvwxyz"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numericApproach = "1234567890"
symbolsCharacters = "[]{}()*&%#@!;:/,_-"

mergeApproaches = lowerCase + upperCase + numericApproach + symbolsCharacters



# Password generator def
def genPass():
    lengthPasswd = input("What is the password length? ")
    passwdFinal = "".join(random.sample(mergeApproaches, int(lengthPasswd)))
    print(passwdFinal)
    tryOther = input("Try again? (y/n) ")
    if tryOther == "y":
        print("\n")
        genPass()
    else:
        print("\n")
        exit()


if __name__ == "__main__":
    genPass()
