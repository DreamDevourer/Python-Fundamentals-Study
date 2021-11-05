# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
# print(student_scores)
# 🚨 Don't change the code above 👆

# Important you are not allowed to use the max() or min() functions. The output words must match the example.

# Write your code below this row 👇
highestNum = student_scores[0]
for score in student_scores:
    if score > highestNum:
        highestNum = score
print(f"The highest score in the class is: {highestNum}")
