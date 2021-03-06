#!/usr/bin/python

import os
import sys
import random
import struct
from Crypto.Cipher import AES

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
 if not out_filename:
  out_filename = in_filename + '.enc'
# iv = ' '.join(chr(random.randint(0, 0xFF)) for i in range(16))
 iv = '1234567890abcdef'
 encryptor = AES.new(key, AES.MODE_CBC, iv)
 filesize = os.path.getsize(in_filename)

 with open(in_filename, 'rb') as infile:
  with open(out_filename, 'wb') as outfile:
   outfile.write(struct.pack('<Q', filesize))
   outfile.write(iv)
 
   while True:
    chunk = infile.read(chunksize)
    if len(chunk) == 0:
     break
    elif len(chunk) % 16 != 0:
     chunk += ' ' * (16 - len(chunk) % 16)
    
    outfile.write(encryptor.encrypt(chunk))


def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
 if not out_filename:
  os.path.splitext(in_filename)[0]
 with open(in_filename, 'rb') as infile:
  origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
  iv = '1234567890abcdef'
  decryptor = AES.new(key, AES.MODE_CBC, iv)
  
  with open(out_filename, 'wb') as outfile:
   while True:
    chunk = infile.read(chunksize)
    if len(chunk) == 0:
     break
    outfile.write(decryptor.decrypt(chunk))
   
   outfile.truncate(origsize)

ac = raw_input("e or d? " )
if ac.lower() == 'e':

 encrypt_file('1234567890abcdef', 'oke.txt')
else:
 decrypt_file('1234567890abcdef', 'oke.txt.enc')
