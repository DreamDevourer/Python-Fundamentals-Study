# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Welcome to the tip calculator.")

billTotal = float(input("What's the bill total? $"))
tipPercentage = int(
    input("Whats is the percentage tip? (0, 10, 12 or 15) ")) / 100
peopleQnty = int(input("How many people to split the bill? "))

totalTip = billTotal * tipPercentage

if tipPercentage > 0:
    mathSolverSum = billTotal + totalTip
    mathSolver = mathSolverSum / peopleQnty
else:
    mathSolver = billTotal / peopleQnty

print(f"Each person should pay: ${round(mathSolver, 2)}")
