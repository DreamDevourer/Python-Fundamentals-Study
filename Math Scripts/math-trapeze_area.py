"""
Interesting resources:
https://docs.python.org/3/library/functions.html#built-in-functions
https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals
https://docs.python.org/3/tutorial/introduction.html#numbers
https://docs.python.org/3/tutorial/modules.html#modules
"""

trapezeShortWidth = input(
    "Enter the width of the short side of the trapezoid: ")
trapezeShortWidth = float(trapezeShortWidth)
trapezeLongWidth = input("Enter the width of the long side of the trapezoid: ")
trapezeLongWidth = float(trapezeLongWidth)
trapezeheight = input("Enter the height of the trapezoid: ")
trapezeheight = float(trapezeheight)

trapezeArea = ((trapezeShortWidth + trapezeLongWidth) / 2) * trapezeheight
print("The area of the trapezoid is: " + str(trapezeArea) + " m2")
