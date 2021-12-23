import base64
import pathlib
import os
import re
import string
from pathlib import Path


os.system("clear")


# Dynamic File Path Solution
API_PATH = pathlib.Path(__file__).parent.absolute()


def relative_to_assets(path: str) -> Path:
    return API_PATH / Path(path)


shiftAlpha = 4
API_CONTENT = None
# 🔐 Security execution READ


def API_SEC():
    global API_CONTENT
    global shiftAlpha

    # Caesar Cipher
    alphaCharset = string.ascii_letters
    numCharset = string.digits
    charsetMain = alphaCharset + numCharset

    totalNum = 0
    for i in range(len(charsetMain)):
        totalNum += i

    shiftAlpha %= totalNum

    unshiftAlpha = -shiftAlpha

    alphaUnshifted = None
    alphaUnshifted = charsetMain[unshiftAlpha:] + charsetMain[:unshiftAlpha]
    tableContentUn = str.maketrans(charsetMain, alphaUnshifted)

    # Security measures
    API_CONTENT = open(relative_to_assets("Data/security/API"), "r").read()
    API_DECODED = base64.b64decode(API_CONTENT.encode("utf-8"))

    # Regular expression to remove garbage characters, do not remove "-"
    API_DECODED_CLEAN = re.sub(
        r"[^A-Za-z0-9-]", "", API_DECODED.decode("utf-8"))

    UNLOCKED_CONTENT = str(API_DECODED_CLEAN).translate(tableContentUn)

    return UNLOCKED_CONTENT


print("\nAdd your API here.\nNEVER CHANGE THE API KEY DIRECTLY\nFOR SECURITY REASONS!\n")
userChange = input("Enter API key: ").strip()

# Caesar Cipher
alphaCharset = string.ascii_letters
numCharset = string.digits
# Combine both alphaCharset with numCharset in one variable
charsetMain = alphaCharset + numCharset

totalNum = 0
for i in range(len(charsetMain)):
    totalNum += i

# print(totalNum)
shiftAlpha = 4
shiftAlpha %= totalNum

alphaShifted = None
alphaShifted = charsetMain[shiftAlpha:] + charsetMain[:shiftAlpha]
tableContent = str.maketrans(charsetMain, alphaShifted)

CIPHER_APPLIED = userChange.translate(tableContent)

# Pick userChange and encode it to base64
userChange = base64.b64encode(CIPHER_APPLIED.encode('utf-8'))
# Save userChange to "API" file
with open(relative_to_assets('Data/security/API'), 'wb') as f:
    # Delete everything inside the file.
    f.truncate()
    f.write(userChange)

    print("DONE! You are ready to use the API!")

userChoice = input("\nDo you want to check the API? (y/n) ").strip()

if userChoice == "y":
    print(f"Your API decoded is: \n{API_SEC()}\nEncoded is: {API_CONTENT}")
else:
    exit()
