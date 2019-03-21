#!/usr/bin/python3

from Crypto.Cipher import AES
import os
import time
import pkg_resources
import random
import daemon
import time
from threading import Thread

filee = 'korban.jpg'#(str(input('nama file : ')))
password = 'passwordpassword'#(str(input('password: ')))

mode = AES.MODE_CBC
iv = 'drowssapdrowssap'#None

def encrypt(password, fileee):
 with open(fileee, 'rb') as kevin:
  text = kevin.read()
  null = 0
  aes = AES.new(password, mode, iv)
  lenn = len(list(text))
  if lenn % 16 != 0:
   while True:
    if len(list(text)) % 16 == 0:
     break
    text += b'\0'  
 text = aes.encrypt(text)
 os.system('rm korban.enc'), os.system('touch korban.enc')
 with open('korban.enc', 'wb') as skara:
  skara.write(text)


def decrypt(mana):
 dec = AES.new('passwordpassword', AES.MODE_CBC, 'drowssapdrowssap')
 with open('korban.enc', 'rb') as pyth:
  text = pyth.read()
  print(type(text))
  decc = dec.decrypt(text)
  decc = decc.rstrip(b"\0")
  with open('korban1.jpg', 'wb') as decry:
   decry.write(decc)

encrypt(password, filee)
decrypt(encc)

   
   
  
