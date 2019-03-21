#!/usr/bin/python

from Crypto.Cipher import AES
import os
import sys
import time

kunci = 'kevinagusto12345'
IV = 'otsuganivek54321'
pesan = 'kevin_agusto1234'
mode = AES.MODE_CBC
enc = AES.new(kunci, mode, IV)
encrypt = enc.encrypt(pesan)
print(encrypt)

dec = AES.new(kunci, mode, IV)
decrypt = dec.decrypt(encrypt)
print(" ")
hasild = decrypt
print(str(hasild))
print(list(str(hasild)))
