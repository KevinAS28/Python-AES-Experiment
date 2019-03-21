#!/usr/bin/python

from Crypto.Cipher import AES
import os
import sys
import random
import time
import struct


def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):

    if not out_filename:
        out_filename = in_filename + '.enc'

#    iv = 'drowssapdrowssap'#''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    encryptor = AES.new(key, AES.MODE_CBC, 'drowssapdrowssap'#iv)
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

encrypt_file('passwordpassword', 'eko.txt', 'eko.enc', 'drowssapdrowssap')




