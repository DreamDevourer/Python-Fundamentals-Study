# Ordinal Numbers to Roman Numbers converter by Nicolas Mendes - September 2021
import sys

# Mapping all Romman numbers combinations
num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

# Function to convert the numbers to roman values. Based on NullDev algorithm.


def num2roman(num):

    roman = ''

    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i

    return roman


# Print roman value.
print(num2roman(int(input("Enter a number: "))))
# After the input, ask if the user wants to continue, and make the default answer to yes.
while True:
    answer = input("Do you want to try again? (Y/n) ")
    if answer == 'y' or answer == 'Y' or sys.stdin.isatty():
        num = int(input("Enter a number: "))
        print(num2roman(num))
    elif answer == 'n':
        break
    else:
        print("Invalid input.")
