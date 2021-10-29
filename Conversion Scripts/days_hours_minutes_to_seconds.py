dayQty = input("How many days? ")
hourQty = input("How many hours? ")
minuteQty = input("How many minutes? ")

print("In " + dayQty + " days, " + hourQty + " hours, and " + minuteQty + " minutes, there are " +
      str(int(dayQty) * 86400 + int(hourQty) * 3600 + int(minuteQty) * 60) + " seconds.")
