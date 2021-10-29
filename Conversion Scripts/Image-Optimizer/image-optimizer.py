""" Script made to optimize PNG, JPG, JPEG and SVG from a folder to make it clean and compressed.
This is not just an experimental script, but a need to my daily work as a DevOps.
"""

import PIL
from PIL import Image
import os
import sys
from pathlib import Path
import pathlib

OUTPUT_PATH = pathlib.Path(__file__).parent.absolute()
ASSETS_PATH = OUTPUT_PATH / Path("original_images")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


files = os.listdir(ASSETS_PATH)

print(f"These are all of the files in our current working directory: {files}")
confirmFiles = input("Confirm files? (Y/n) ")
confirmDownRes = input("Do you want to reduce the resolution by 50%? (Y/n) ")


if confirmDownRes == "y" or confirmDownRes == "Y" or confirmDownRes == "":
    confirmReduction = True

if confirmFiles == "y" or confirmFiles == "Y" or confirmFiles == "":
    for file in files:
        if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
            print(f"Optimizing {file}")
            imgOptimize = Image.open(relative_to_assets(str(file)))
            imgWidth, imgHeight = imgOptimize.size
            if confirmReduction == True:
                imgOptimize = imgOptimize.resize(
                    (int(imgWidth / 2), int(imgHeight / 2)), PIL.Image.ANTIALIAS)

                if file.endswith(".png"):
                    imgOptimize.save(str(relative_to_assets(
                        str(file))), optimize=True, quality=70)
                if file.endswith(".jpg") or file.endswith(".jpeg"):
                    imgOptimize.save(str(relative_to_assets(
                        str(file))), optimize=True, quality=80)
            else:
                if file.endswith(".png"):
                    imgOptimize.save(str(relative_to_assets(
                        str(file))), optimize=True, quality=70)
                if file.endswith(".jpg") or file.endswith(".jpeg"):
                    imgOptimize.save(str(relative_to_assets(
                        str(file))), optimize=True, quality=80)
            print(f"{file} optimized!")
        else:
            print(f"{file} is not a PNG or JPG, skipping")
else:
    print("Exiting...")
    sys.exit()

# Testing modules
# imgOptimize = Image.open(files)
# imgHeight, imgWidth = imgOptimize.size
# imgOptimize = imgOptimize.resize((int(imgWidth / 2), int(imgHeight / 2)), PIL.Image.ANTIALIAS)
# imgOptimize.save(ASSETS_PATH / Path("optimized_images/optimized_image.png"), optimize=True, quality=95)
