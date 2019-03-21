from Crypto.Cipher import AES
import os
import sys
from getpass import getpass

spab = (lambda x: [print(' ') for i in range(x)])
filee = input('nama file: ')
mode = AES.MODE_CBC
mode1 = AES.MODE_CFB
mode2 = AES.MODE_XTS
password = ''
def kata():
 global password
 password = input('password dong: ')#'passwordpassword'

while len(password) != 16:
 print('password harus 16 byte')
 kata()
iv = 'drowssapdrowssap'

dec1 = AES.new(password, mode, iv)
dec2 = AES.new(password, mode1, iv)
dec3 = AES.new(password, mode2, iv)
def decrypt():
 with open(filee, 'rb') as pyth:
  oke = pyth.read()
  oke = dec3.decrypt(oke)
  oke = dec2.decrypt(oke)
  oke = dec1.decrypt(oke)
  oke = oke.rstrip(b"\0")
  asli = filee.replace('.enc', '')
  open(asli, 'w+')
  cek = os.access(asli, os.W_OK)
  if cek == False:
   print('file baru tidak bisa diakses')
   sys.exit()
  with open(asli, 'wb') as jadi:
   jadi.write(oke)
  os.remove(filee)

decrypt()
spab(5)
print('proses dekripsi selsai.by kevin as.')
