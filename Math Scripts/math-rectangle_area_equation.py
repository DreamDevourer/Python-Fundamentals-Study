"""
Interesting resources:
https://docs.python.org/3/library/functions.html#built-in-functions
https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals
https://docs.python.org/3/tutorial/introduction.html#numbers
https://docs.python.org/3/tutorial/modules.html#modules
"""


def welcome():
    print("Welcome! Let's calculate the rectagle.")
    units = input(
        "Please enter the units to use (square meters or centimeters): ")

    if units == "square meters":
        width = float(
            input("Please enter the width of the rectangle in meters: "))
        height = float(
            input("Please enter the height of the rectangle in meters: "))
        print("The area of the rectangle is: ",
              width * height, "square meters")
        startAgain()
    elif units == "centimeters":
        width = float(
            input("Please enter the width of the rectangle in centimeters: "))
        height = float(
            input("Please enter the height of the rectangle in centimeters: "))
        print("The area of the rectangle is: ", width * height, "centimeters")
        startAgain()
    else:
        print("Please enter a valid input.")


def startAgain():
    retryCalc = input("Would you like to calculate another rectangle? (y/n): ")
    if retryCalc == "y":
        welcome()
    elif retryCalc == "n":
        print("Thank you for using this program.")
    else:
        print("Please enter a valid input.")


if __name__ == "__main__":
    welcome()
