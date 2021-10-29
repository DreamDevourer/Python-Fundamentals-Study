"""
Interesting resources:
https://docs.python.org/3/library/functions.html#built-in-functions
https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals
https://docs.python.org/3/tutorial/introduction.html#numbers
https://docs.python.org/3/tutorial/modules.html#modules
"""

circleRay = float(input("Enter the circle's radius in square meters: "))
# Calculate the circle's area in square meters
circleArea = circleRay ** 2 * 3.14159
# Print the circle's area in square meters
print("The circle's area is {:.2f} m2.".format(circleArea))
