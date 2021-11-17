# Objective: Generate a band name from city and pet name.

import random
# 1. Create a greeting for your program.
print(
    "Hello, welcome to Band Name Generator"
)
# 2. Ask the user for the city that they grew up in.
cityInfo = input("What is the city you grew up?\n")
print("Awesome! \n")
# 3. Ask the user for the name of a pet.
petInfo = input("Type a pet name:\n")
petMSGs = {"msg1": "Great name!", "msg2": "Amazing!",
           "msg3": "Interesting name.", "msg4": "Wow, that's great!"}
print(f"{random.choice(list(petMSGs.values()))}\n")
megaFusion = cityInfo+" "+petInfo
# 4. Combine the name of their city and pet and show them their band name.
print(f"Your band name could be: {megaFusion}")

# 5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/
