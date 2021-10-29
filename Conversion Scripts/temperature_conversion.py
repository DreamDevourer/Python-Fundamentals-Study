print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
whatType = input("What temperature scale do you want to convert from? ")

if whatType == "1":
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = celsius * 9 / 5 + 32
    print("The temperature in Fahrenheit is", fahrenheit)
elif whatType == "2":
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print("The temperature in Celsius is", celsius)
else:
    print("Invalid input")
    print("Please try again")
