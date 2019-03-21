#!/usr/bin/python3

import os
from Crypto.Cipher import AES
import sys

#os.chdir('aes')
class encrypt:
 def __init__(self, filee):
  self.filee = filee
  self.key = 'kevinagusto12345'
  self.iv =  'otsuganivek54321'
  self.mode = AES.MODE_CBC
  self.aes = AES.new(self.key, self.mode, self.iv)
 def enc(self):
  chk = os.access(self.filee, os.W_OK)
  if not chk:
   print('nulis yang bener ngapah')
   sys.exit()
  with open(self.filee, 'rb') as pyth:
   oke = pyth.read()
   if (len(oke) % 16) != 0:
    while 1:
     if (len(oke) % 16) == 0:
      break
     oke += b'\0'
   jadi = self.aes.encrypt(oke)
   with open(self.filee + '.enc', 'wb') as nice:
    nice.write(jadi)
    os.remove(self.filee)

class decrypt(encrypt):
 def dec(self):
  chk1 = os.access(self.filee, os.W_OK)
  if not chk1:
   sys.exit()
   print('males ah')
  with open(self.filee, 'rb') as nice:
   eko = nice.read()
   eko = self.aes.decrypt(eko)
   eko = eko.replace(b'\0', '')
   name1 = self.filee.replace('.enc', '')
   with open(name1, 'wb') as wow:
    wow.write(eko)
    os.remove(self.filee)
   


startt = decrypt('korban1.txt.enc')
startt.dec()


   

