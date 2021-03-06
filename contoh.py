from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto import Random

key_size = 32 #AES256
iterations = 10000
key = b'password'
secret = b'a very secret message'

length = 16 - (len(secret) % 16) #PKCS7 adds bytes of the length of padding
secret += chr(length) * length

salt = Random.new().read(key_size) #salt the hash
iv = Random.new().read(AES.block_size)
derived_key = PBKDF2(key, salt, key_size, iterations)
cipher = AES.new(derived_key, AES.MODE_CBC, iv)

encodedtext = iv + cipher.encrypt(secret)
decodedtext = str(cipher.decrypt(encodedtext))[16:-ord(decodedtext[-1])] #remove iv and padding

def spab(x):
 for abc in range(x):
  print(' ')

print(encodedtext)
spab(3)
print(decodedtext)
