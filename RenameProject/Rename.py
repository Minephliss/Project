import os
import random
import shutil

def change(value):
    if value > 9:
        return chr(value - 10 + ord('A'))
    return str(value)

dirname = './' + input('Input the directory\'s name that you are about to operate:') + '/'
basename = input('The target name is:')

filelist = os.listdir(dirname)

print(filelist)

for file in filelist:
    tarname = dirname
    for i in range(0, 32):
        tarname += change(int(random.random() * 100) % 16)
    tarname += '.jpg'
    os.rename(dirname + file, tarname)

shutil.make_archive('./' + basename,'zip', './', dirname)

print ('Done!')
