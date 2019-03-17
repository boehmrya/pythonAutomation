
import shutil
import os

'''
for filename in os.listdir():
    if filename.endswith('.txt'):
        os.unlink(filename)
        print(filename)
'''

for folderName, subfolders, filenames in os.walk('.'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')
