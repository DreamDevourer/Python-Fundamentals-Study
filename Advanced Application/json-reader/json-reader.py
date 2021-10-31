import json
import sys
import os

userContent = {}
current_dir = os.path.dirname(sys.argv[0])

with open(f"{current_dir}/sample-json.json", "r") as json_file:
    userContent = json.load(json_file)
    print(userContent["username"])
    print(userContent["password"])

userInp = input("Enter your username: ")
userInp2 = input("Enter your password: ")
userContent["username"] = f"{str(userInp)}"
userContent["password"] = f"{str(userInp2)}"


with open(f"{current_dir}/sample-json.json", "w") as json_file:
    json.dump(userContent, json_file)
    print("The new username is: " + str(userContent["username"]))
    print("The new password is: " + str(userContent["password"]))
