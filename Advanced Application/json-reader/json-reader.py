import json
import sys
import os

userContent = {}

with open("sample-json.json", "r") as json_file:
    userContent = json.load(json_file)
    print(userContent["username"])
    print(userContent["password"])

userInp = input("Enter your username: ")
userInp2 = input("Enter your password: ")
userContent["password"] = f"{str(userInp2)}"


with open("sample-json.json", "w") as json_file:
    json.dump(userContent, json_file)
    print("The new password is: " + str(userContent["password"]))
