#!/usr/bin/python

from Crypto.Cipher import AES
#oke = input("e or d? ")




if True:#oke.lower() == 'e':
 key = '1234567890abcdef'
 IV = 16 * '\x00'
 mode = AES.MODE_CBC
 encryptor = AES.new(key, mode, IV=IV)

 text = 'kevinkevinkevin1'
 ciphertext = encryptor.encrypt(text)
 print ciphertext

oke = input("apa ? ")

if oke.lower() == 'd':
 key = '1234567890abcdef'
 IV = 16 * '\x00'
 mode = AES.MODE_CBC
 decryptor = AES.new(key, mode, IV=IV)

# text = 'kevinkevinkevin1'
 ciphertext1 = decryptor.decrypt(ciphertext).decode('utf-8')
 print ciphertext1





#oke = input("E / D? ")
#if oke.lower == 'e':





