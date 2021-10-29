""" Made by Nicolas Mendes September 26 2021
Study to understand how JPG/JPEG files work in HEX form and how to hide a string in a JPG file.
Basically JPG images ALWAYS start with "FF D8 FF" and ends with "FF D9". That means we can append a string
on the end of this sequence "FF D9".
"""
import pathlib
from pathlib import Path
import string


"""
    0xffd8: "Start of Image",
    0xffe0: "Application Default Header",
    0xffdb: "Quantization Table",
    0xffc0: "Start of Frame",
    0xffc4: "Define Huffman Table",
    0xffda: "Start of Scan",
    0xffd9: "End of Image"
"""

# Initial Setup to load assets
OUTPUT_PATH = pathlib.Path(__file__).parent.absolute()
ASSETS_PATH = OUTPUT_PATH / Path("./hideJPG")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


while True:

    def writeString():
        with open(relative_to_assets('photo.jpg'), 'ab') as f:  # ab append bytes mode
            f.write(b' Hidden message: test :)')

    def readString():
        with open(relative_to_assets('photo.jpg'), 'rb') as f:  # Read bytes mode
            jpgContent = f.read()
            # when FF D9 occurs.
            offset = jpgContent.index(bytes.fromhex('FFD9'))
            f.seek(offset + 2)
            print(f.read())

    def deleteString():
        # delete everything after the last FF D9
        with open(relative_to_assets('photo.jpg'), 'r+') as f:  # Read bytes mode
            jpgContent = f.read()
            offset = jpgContent.index(bytes.fromhex('FFD9'))
            f.seek(offset + 2)
            f.truncate()

    # Check if photo.jpg exists and print it.
    if relative_to_assets("photo.jpg").exists():
        print("Found photo.jpg")
        readMessage = input(
            "Do you want to read, write or delete a message? (r/w/d) ")
        if readMessage == "r":
            readString()
        if readMessage == "w":
            writeString()
        if readMessage == "d":
            deleteString()

    else:
        print("Could not find photo.jpg")
