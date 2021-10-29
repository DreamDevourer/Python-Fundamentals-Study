import os
import time
import sys
import subprocess


current_dir = os.path.dirname(sys.argv[0])
targetDirectory = "test"
fixDirPath = current_dir.replace(" ", "\\ ").replace("?", "\\?").replace("&", "\\&").replace(
    "(", "\\(").replace(")", "\\)").replace("*", "\\*").replace("<", "\\<").replace(">", "\\>")

dailyTimer = 10
enableCustomHour = True
customHour = "03:00PM"

userCorrect = None

print(f"{fixDirPath}/{targetDirectory}")
userPermission = input("What is the password? \n")


def deleteFiles():
    if userCorrect == False:
        print("Deleting files...")
        os.system(f"rm -rf {str(fixDirPath)}/{str(targetDirectory)}")

    # if enableCustomHour:
    #     if customHour == time.strftime("%I:%M%p"):
    #         print("Time to delete files!")
    #         os.system("rm -rf " + str(targetDirectory))
    # else:
    #     pass


if userPermission != "AbC=CdE":
    print("Incorrect password... Cleaning process initiated!")
    userCorrect = False
    deleteFiles()

elif userPermission == "AbC=CdE":
    print("Thank you!")
    userCorrect = True
    exit()
