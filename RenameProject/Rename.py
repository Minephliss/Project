import os
import random

def change(value):
    if value > 9:
        return chr(value - 10 + ord('A'))
    return str(value)

dirname = './' + input('Input the directory\'s name that you are about to operate:') + '/'

filelist = os.listdir(dirname)
for file in filelist:
    tarname = dirname
    for i in range(0, 32):
        tarname += change(int(random.random() * 100) % 16)
    tarname += '.jpg'
    os.rename(dirname + file, tarname)

print ('Done!')
