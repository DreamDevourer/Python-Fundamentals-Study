secsQty = input("Enter the number of seconds: ")
secsQty = int(secsQty)

# convert seconds in minutes.
minutes = secsQty // 60
# convert seconds in hours.
hours = minutes // 60
# convert seconds in days.
days = hours // 24

print(str(secsQty) + " seconds is equal to " + str(minutes) + " minutes, " +
      str(hours) + " hours, and " + str(days) + " days.")
