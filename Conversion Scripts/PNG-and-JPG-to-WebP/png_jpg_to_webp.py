""" Script made to convert PNG or JPG from a folder to WebP format.
This is not just an experimental script, but a need to my daily work as a DevOps.
"""

from PIL import Image
import os
import sys
from pathlib import Path
import pathlib


OUTPUT_PATH = pathlib.Path(__file__).parent.absolute()
ASSETS_PATH = OUTPUT_PATH / Path("original_images")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Testing modules
# loadImg = Image.open(relative_to_assets("image_test.jpg")).convert("RGB")
# loadImg.save(relative_to_assets("image_test.webp"), "WEBP", quality=80)


# We list all of the files and folders using os.listdir()
files = os.listdir(ASSETS_PATH)   

print(f"These are all of the files in our current working directory: {files}")
confirmFiles = input("Confirm files? (Y/n) ")

if confirmFiles == "y" or confirmFiles == "Y" or confirmFiles == "":
    for file in files:
        if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
            print(f"Converting {file} to WebP")
            loadImg = Image.open(relative_to_assets(str(file)))
            loadImg.save(str(relative_to_assets(str(file))) +
                         ".webp", "WEBP", quality=80)
            print(f"{file} converted to WebP")
        else:
            print(f"{file} is not a PNG or JPG, skipping...")
else:
    print("Exiting...")
    sys.exit()
