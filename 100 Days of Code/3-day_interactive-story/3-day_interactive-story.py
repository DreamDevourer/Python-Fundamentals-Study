print('''
*******************************************************************************
     .  . '    .                                             
      '   .            . '            .                +           
              `                          '    . '
        .                         ,'`.                         .
   .                  .."    _.-;'    `.              .    
              _.-"`.##%"_.--" ,'        `.           "#"     ___,,od000
           ,'"-_ _.-.--"\   ,'            `-_       '%#%',,/////00000HH
         ,'     |_.'     )`/-     __..--""`-_`-._    J L/////00000HHHHM
 . +   ,'   _.-"        / /   _-""           `-._`-_/___\///0000HHHHMMM
     .'_.-""      '    :_/_.-'                 _,`-/__V__\0000HHHHHMMMM
 . _-""                         .        '   _,////\  |  /000HHHHHMMMMM
_-"   .       '  +  .              .        ,//////0\ | /00HHHHHHHMMMMM
       `                                   ,//////000\|/00HHHHHHHMMMMMM
.             '       .  ' .   .       '  ,//////00000|00HHHHHHHHMMMMMM
     .             .    .    '           ,//////000000|00HHHHHHHMMMMMMM
                  .  '      .       .   ,///////000000|0HHHHHHHHMMMMMMM
  '             '        .    '         ///////000000000HHHHHHHHMMMMMMM
                    +  .  . '    .     ,///////000000000HHHHHHHMMMMMMMM
     '      .              '   .       ///////000000000HHHHHHHHMMMMMMMM
   '                  . '              ///////000000000HHHHHHHHMMMMMMMM
                           .   '      ,///////000000000HHHHHHHHMMMMMMMM
       +         .        '   .    .  ////////000000000HHHHHHHHMMMMMMhs
*******************************************************************************
''')
print("Welcome to Titan Station.")
print("Your mission is to find the Marker, a black monolith.")

#Write your code below this line 👇

def startChoice():
	choice1 = input('You are orbiting the station, everything seems calm, what do you want to do? Type "dock" to dock your ship into the docking bay or "watch" \n').lower()

	if choice1 == "dock":
		choice2 = input('You\'ve docked your ship. Everything is quiet and dark. Type "gov sector" to go to the government sector for looking to the marker or type "explore" to explore the nearby corridors. \n').lower()
		if choice2 == "gov sector":
			choice3 = input("You reached the government sector bulk door. An Earthgov soldier asks for the password? (you have a note about the marker, probably the password can be 'Tiedemann', 'Marshal Law', 'Isaac Clark') \n").lower()
			if choice3 == "Tiedemann":
				print("The soldiers disappear and an horde of necromorphs catches you. Game Over.")
			elif choice3 == "Marshal Law":
				print("You entered the Earthgov sector and now you have access to the black marker! You Win!")
			elif choice3 == "Isaac Clark":
				print("The soldier calls for reinforcements and then shoot you. Game Over.")
			else:
				print("You chose a door that doesn't exist. Game Over.")
		else:
			print("You get attacked by a hidden necromorph in the dark. Game Over.")
	else:
		print("You have been hit by an asteroid, your ship exploded. Game Over.")

startChoice()
