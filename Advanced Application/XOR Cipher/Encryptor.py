#! /usr/bin/env python3
import base64
import os
import pathlib
import re
from pathlib import Path

# Nick's security protocol
os.system("clear")

# Dynamic File Path Solution
KEY_PATH = pathlib.Path(__file__).parent.absolute()


def relative_to_assets(path: str) -> Path:
    return KEY_PATH / Path(path)


def encryptSecurity():
    # Use external script to make base64 or https://www.base64encode.org/
    key = "MTMy"  # up 255
    key = base64.b64decode(key)
    cleanKey = re.sub(
        r"[^A-Za-z0-9-]", "", key.decode("utf-8"))
    finalKey = int(cleanKey)

    loadEnc00 = open(relative_to_assets("Data/security/.KEY"), "rb")
    byteReaderData = loadEnc00.read()
    loadEnc00.close()

    byteReaderData = bytearray(byteReaderData)
    for index, value in enumerate(byteReaderData):
        byteReaderData[index] = value ^ finalKey

    Enc = open(relative_to_assets("Data/security/.KEY.nclmE"), "wb")
    Enc.write(byteReaderData)
    Enc.close()

    # Delete Data/security/KEY
    os.remove(relative_to_assets("Data/security/.KEY"))


encryptSecurity()
