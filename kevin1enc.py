from Crypto.Cipher import AES
import os
from getpass import getpass

osnya = os.name
filee = input("nama file: ")
spab = (lambda x: [print(" ") for i in range(x)])
spab(2)
#ofb = AES.MODE_OFB
cbc = AES.MODE_CBC
sandi = ''
def kata():
 global sandi
 sandi = input('password dong: ')#'passwordpassword'

while len(sandi) != 16:
 print('password harus 16 byte')
 kata()
iv = 'drowssapdrowssap'
exist = os.access(filee, os.W_OK)
if exist == False:
 print

def rang():
 global null
 global nol
 null = 0
 nol = 0

def encrypt():
 with open(filee, 'rb') as pyth:
  oke = pyth.read()
  enc = AES.new(sandi, cbc, iv)
#  enc1 = AES.new(sandi, ofb, iv)
  if len(oke) % 16 != 0:
   while True:
    if len(oke) % 16 == 0:
     break
    oke += b"\0"
  jadi = enc.encrypt(oke)
  open((filee + ".enc"), 'w+')
  with open(filee + ".enc", 'wb') as tulis:
   tulis.write(jadi)
  os.remove(filee)

encrypt()
spab(5)
print('cryptography success, by kevin as')
  
