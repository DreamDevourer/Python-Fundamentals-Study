#! /usr/bin/env python3
import base64
import os
import pathlib
import re
import string
from pathlib import Path
import signal

# Nick's security protocol
os.system("clear")

# Dynamic File Path Solution
KEY_PATH = pathlib.Path(__file__).parent.absolute()


def relative_to_assets(path: str) -> Path:
    return KEY_PATH / Path(path)


def signal_handler(sig, frame):
    # If the program exits then remove important files.
    os.remove(relative_to_assets("Data/security/.tmp/.KEY"))
    exit()


def decryptSecurity():
    # Use external script to make base64 or https://www.base64encode.org/
    key = "MTMy"  # up 255
    key = base64.b64decode(key)
    cleanKey = re.sub(
        r"[^A-Za-z0-9-]", "", key.decode("utf-8"))
    finalKey = int(cleanKey)

    loadEnc00 = open(relative_to_assets(
        "Data/security/.KEY.nclmE"), "rb").read()

    byteReader = bytearray(loadEnc00)
    for index, value in enumerate(byteReader):
        byteReader[index] = value ^ finalKey

    decEnc = open(relative_to_assets("Data/security/.tmp/.KEY"), "wb")
    decEnc.write(byteReader)


try:
    # signal handler for "CTRL + C"
    signal.signal(signal.SIGINT, signal_handler)
    decryptSecurity()
    signal.pause()
except:
    # Before exit the script will remove decrypted files.
    os.remove(relative_to_assets("Data/security/.tmp/.KEY"))
