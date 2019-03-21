#!/usr/bin/python

from Crypto.Cipher import AES
import sys
import os
import base64
import time

#kan baru pemula
#encrypt, trus kasih waktu, waktu habis = delete

size = 16
pad = '{'
IV = 'passwordpassword'

def padd(s):
 s + (size - len(s) % size) * pad

def encoaes(c, s):
 base64.b64encode(c.encrypt(padd(s)))

def decoaes(c, e):
 c.decrypt(base64.b64decode(e)).rstrip(pad)

secrett = 'passwordpassword'
secret = secrett.encode("latin-1")
cipher = AES.new(secret, AES.MODE_CBC, IV)

encrypt = encoaes(cipher, secret)
print("encrypt = %s" %(encrypt))

decrypt = decoaes(cipher, encrypt)
print("decrypted = %s" %(decrypt))
