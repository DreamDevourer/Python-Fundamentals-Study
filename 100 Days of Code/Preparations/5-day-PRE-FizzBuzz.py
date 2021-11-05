#Write your code below this row 👇

fizzMsg = "FIZZ"
buzzMSG = "BUZZ"
fizzBuzzMSG = "FIZZBUZZ"

for fB in range(1, 101):
	
	if fB % 3 == 0 and fB % 5 == 0:
		print(fizzBuzzMSG)
	elif fB % 5 == 0:
		print(buzzMSG)
	elif fB % 3 == 0:
		print(fizzMsg)
	else:
		print(fB)
