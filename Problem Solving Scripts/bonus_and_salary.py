"""
The employees of a company will receive a 5% salary increase and a bonus at the end of the year equivalent to 20% of the new salary.
"""

bonusQuantity = 5
endOfYearPercentage = 20

employeeSalary = float(input("Enter the employee's salary: "))
# Calculate the percentage employeeSalary with bonusQuantity
bonus = employeeSalary * bonusQuantity / 100
# Calculate the percentage employeeSalary with endOfYearPercentage
endOfYear = employeeSalary * endOfYearPercentage / 100
# Calculate the new salary
newSalary = employeeSalary + bonus + endOfYear
print("With the bonus it will be: ", bonus + employeeSalary)
print("With the end of year it will be: ", endOfYear + employeeSalary)
print("Final salary is: ", newSalary)
