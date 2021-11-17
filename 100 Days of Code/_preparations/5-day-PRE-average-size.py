# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.


#Write your code below this row 👇
masterSum = 0
for sum in student_heights:
  masterSum += sum
# print(masterSum)

totalItems = 0
for totalNum in student_heights:
	totalItems += 1
# print(totalItems)

calcFinal = masterSum/totalItems
print(f"Average size: {calcFinal}cm")
